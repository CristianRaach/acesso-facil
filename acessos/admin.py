from django.contrib import admin
from .models import cadastro_acesso, config_geral, config_comunicacao

admin.site.register(cadastro_acesso)
admin.site.register(config_geral)
admin.site.register(config_comunicacao)
