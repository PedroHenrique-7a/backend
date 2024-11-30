from django.urls import path
from .views import fprodutos, fcadproduto, salvar, editar, excluir, update

urlpatterns = [

    path('', fprodutos),
    path('fcadproduto/', fcadproduto, name='fcadproduto'),
    path('salvar/', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update')
    ]