from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import cadastro_acesso, config_geral, config_comunicacao
from .form import AcessoForm, RecuperarSenha, AcessoForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .utils import *
import requests


@login_required
def lista_acessos(request):
    if membro_da_equipe(request.user):
        acessos = cadastro_acesso.objects.order_by('ativo')
        #geral = config_geral.objects.get(pk=1)
        #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
        geral = ''
        cor_menu = ''

        busca = request.GET.get('search')
        if busca:
            if isnumber(busca):
                acessos = cadastro_acesso.objects.filter(cpf__icontains = busca)
            else:
                acessos = cadastro_acesso.objects.filter(nome__icontains = busca)

        return render(request, 'list.html', {'acessos': acessos, 'geral': geral, 'cor_menu': cor_menu})

    return redirect('acessar')


@login_required
def novo_acesso(request):
    if membro_da_equipe(request.user):
        form = AcessoForm(request.POST or None, request.FILES or None)
        #geral = config_geral.objects.get(pk=1)
        #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
        geral = ''
        cor_menu = ''

        if form.is_valid():
            #print(form['cpf'].data)
            user = User.objects.create_user((form['cpf'].data), (form['email'].data), (form['senha'].data))
            user.last_name = 'usuariocomum'
            user.first_name = form['nome'].data
            user.save()
            form.save()

            return redirect('lista')
        return render(request, 'acesso_form.html', {'form': form, 'geral': geral, 'cor_menu': cor_menu})

    return redirect('acessar')


@login_required
def alterar_acesso(request, id):
    if membro_da_equipe(request.user):
        cadastro = get_object_or_404(cadastro_acesso, pk=id)
        form = AcessoForm(request.POST or None, request.FILES or None, instance=cadastro)
        #geral = config_geral.objects.get(pk=1)
        #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
        geral = ''
        cor_menu = ''

        username = cadastro.cpf

        if form.is_valid():
            user = User.objects.get(username=username)
            user.first_name = form['nome'].data
            user.username = form['cpf'].data
            user.set_password(form['senha'].data)
            user.save()
            #print (form['nome'].data)
            form.save()
            return redirect('lista')

        return render(request, 'acesso_form.html', {'form': form, 'cadastro': cadastro, 'cor_menu': cor_menu})
    
    return redirect('acessar')


@login_required
def desativar_acesso(request, id):
    if membro_da_equipe(request.user):
        cadastro = get_object_or_404(cadastro_acesso, pk=id)
        action = 'desativar'
        #geral = config_geral.objects.get(pk=1)
        #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
        geral = ''
        cor_menu = ''

        if request.method == 'POST':
            cadastro.ativo = False
            cadastro.save()
            return redirect('lista')

        return render(request, 'acesso_desativar.html', {'cadastro': cadastro, 'action': action, 'geral': geral, 'cor_menu': cor_menu})

    return redirect('acessar')


@login_required
def ativar_acesso(request, id):
    if membro_da_equipe(request.user):
        cadastro = get_object_or_404(cadastro_acesso, pk=id)
        action = 'ativar'
        #geral = config_geral.objects.get(pk=1)
        #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
        geral = ''
        cor_menu = ''

        if request.method == 'POST':
            cadastro.ativo = True
            cadastro.save()
            return redirect('lista')

        return render(request, 'acesso_desativar.html', {'cadastro': cadastro, 'action': action, 'geral': geral, 'cor_menu': cor_menu})

    return redirect('acessar')


def esqueci_senha(request):
    form = RecuperarSenha(request.POST or None, request.FILES or None)
    #geral = config_geral.objects.get(pk=1)
    #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
    geral = ''
    cor_menu = ''

    if request.method == 'POST':
        print(form['cpf'].data)
        cadastro = cadastro_acesso.objects.get(cpf=form['cpf'].data)
        print(cadastro.nome)
        print(cadastro.celular)
        print(cadastro.email)
        return redirect('login')

    return render(request, 'esqueci_senha.html', {'form': form, 'geral': geral, 'cor_menu': cor_menu})
    

def home(request):
    geral = config_geral.objects.get(pk=1)

    return redirect('login', {'geral': geral})


@login_required
def acessar(request):
    #geral = config_geral.objects.get(pk=1)
    #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
    geral = ''
    cor_menu = ''


    #url = "http://tisul.no-ip.info:8989/login"
    #content = "{\"cpf\": \"90916743004\",\"senha\": \"1234\"}"
    #headers = {
    #    'user-agent': "vscode-restclient",
    #    'content-type': "application/json"
    #    }
    #try:
    #    response = requests.request("GET", url, data=content, headers=headers)

    #    data = response.json()
    #except:
    #    data = ""
    data = ""

    acessos = get_object_or_404(cadastro_acesso, cpf=request.user)
        
    return render(request, 'qr_code.html', {'acessos': acessos, 'data': data, 'geral': geral, 'cor_menu': cor_menu})


def login_view(request):
    nome = request.POST.get('username')
    senha = request.POST.get('password')
    user = authenticate(request, username=nome, password=senha)

    ########
    #geral = config_geral.objects.order_by('id')
    #if geral:
    #    action = 'Seja Bem Vindo a ' + (geral.nome_empresa)
    #else:
    action = 'Seja Bem Vindo a sua empresa'
    #cor_login = '<div class="login-spy" style="background-color:' + (geral.cor_login) + ';" >'
    #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
    cor_login = ''
    cor_menu = ''

    if user is not None:
        login(request, user)
        
        if membro_da_equipe(request.user):
            acessos = cadastro_acesso.objects.order_by('ativo')
            

            return render(request, 'list.html', {'acessos': acessos, 'cor_menu': cor_menu})

        return redirect('acessar')
    else:
        return render(request, 'login_logout.html', {'action': action, 'cor_login': cor_login})


def logout_view(request):
    logout(request)
    
    #cor_login = '<div class="login-spy" style="background-color:' + (geral.cor_login) + ';" >'
    #cor_menu = '<nav id="menus" style="background-color:' + (geral.cor_menu) + ';" >'
    cor_login = ''
    cor_menu = ''

    action = 'Sua empresa' + '<br>' +'Agradece pela Visita!'
    
    return render(request, 'login_logout.html', {'action': action, 'cor_login': cor_login})