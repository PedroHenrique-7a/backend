"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from .views import fcliente, Fcadcliente, salvar_cli, exibir_cli, excluir_cli, login, ftelacli, logar, Frel
urlpatterns = [
    path('', fcliente),
    path('Fcadcliente/',Fcadcliente, name='Fcadcliente'),
    path('salvar_cli/', salvar_cli, name='salvar_cli'),
    path('excluir_cli/<int:id>', excluir_cli, name='excluir_cli'),
    path('exibir_cli/<int:id>', exibir_cli, name='exibir_cli'),
    path('login/', login, name='login'),
    path('ftelacli/', ftelacli, name='ftelacli'),
    path('Frel/', Frel, name='Frel'),
    path('logar/', logar, name='logar')

]