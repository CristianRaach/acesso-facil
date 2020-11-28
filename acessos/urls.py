from django.urls import path
from acessos.views import lista_acessos, novo_acesso, alterar_acesso, desativar_acesso
from .views import home, esqueci_senha, acessar, ativar_acesso, login_view, logout_view


urlpatterns = [
    path('lista/', lista_acessos, name="lista"),
    path('novo/', novo_acesso, name="novo"),
    path('alterar/<int:id>/', alterar_acesso, name="alterar"),
    path('desativar/<int:id>/', desativar_acesso, name="desativar"),
    path('ativar/<int:id>/', ativar_acesso, name="ativar"),
    path('esqueceu_senha/', esqueci_senha, name="esqueci"),
    path('', login_view , name="login"),
    path('logout/', logout_view , name="logout"),
    path('acesso/', acessar, name="acessar"),
]
