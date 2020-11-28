from django.db import models

class cadastro_acesso(models.Model):
    cpf = models.CharField(max_length=11, unique=True, help_text="Por favor insira um CPF válido, somente números.")
    nome = models.CharField(max_length=30)
    senha = models.CharField(max_length=8)
    celular = models.CharField(max_length=11, help_text="Por favor insira somente números. Ex.51999999999")
    email = models.EmailField()
    obs = models.TextField(max_length=150, null=True, blank=True)
    data_ini = models.DateTimeField ( auto_now = False , auto_now_add = False)
    data_fim = models.DateTimeField ( auto_now = False , auto_now_add = False)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos_cadastros', null=True, blank=True)


    def __str__(self):
        return self.nome + ' - CPF: ' + self.cpf + ' - Senha: ' + self.senha + ' - Celular: ' + self.celular 

class config_geral(models.Model):
    nome_empresa = models.CharField(max_length=30, null=True, blank=True)
    cor_login = models.CharField(max_length=10, null=True, blank=True)
    cor_main = models.CharField(max_length=10, null=True, blank=True)
    cor_menu = models.CharField(max_length=10, null=True, blank=True)
    obs = models.TextField(max_length=150, null=True, blank=True)
    foto_bg = models.ImageField(upload_to='fotos_cadastros', null=True, blank=True)
    foto_logo = models.ImageField(upload_to='fotos_cadastros', null=True, blank=True)


    def __str__(self):
        return self.nome_empresa


class config_comunicacao(models.Model):
    user = models.CharField(max_length=50, null=True, blank=True)
    senha = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    email_copia = models.EmailField()
    porta = models.IntegerField
    smtp = models.CharField(max_length=50, null=True, blank=True)
    autenticacao = models.BooleanField(default=True)
    ssl = models.BooleanField(default=True)
    obs = models.TextField(max_length=150, null=True, blank=True)


    def __str__(self):
        return self.user 