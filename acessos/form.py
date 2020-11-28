from django.forms import ModelForm, CharField, TextInput, RegexField
from .models import cadastro_acesso

class AcessoForm(ModelForm):
    
    cpf = RegexField(regex=r'^[0-9]+$', error_messages = {'invalid_number':'Por favor insira um CPF válido, somente números.'}, min_length=11)
    celular = RegexField(regex=r'^[0-9]+$', error_messages = {'invalid_phonenumber':"Por favor insira somente números. Ex.51999999999"})
    senha = RegexField(regex=r'^[0-9]+$', error_messages = {'invalid_number':'Por favor insira 4 dígitos.'}, min_length=4, max_length=4)
    class Meta:
        model = cadastro_acesso
        fields = ['nome', 'celular', 'email', 'cpf', 'senha', 'data_ini', 'data_fim', 'foto' , 'obs']


class RecuperarSenha(ModelForm):
    
    cpf = RegexField(regex=r'^[0-9]+$', error_messages = {'invalid_number':'Por favor insira um CPF válido, somente números.'})
    
    class Meta:
        model = cadastro_acesso
        fields = ['cpf']        