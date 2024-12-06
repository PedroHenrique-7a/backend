from django.urls import path
from .views import fprodutos, fcadproduto, salvar, editar, excluir, update, flista_produtos
from django.conf.urls.static import static
from django.conf import settings
app_name='produto'

urlpatterns = [

    path('', fprodutos, name='fprodutos'),
    path('fcadproduto/', fcadproduto, name='fcadproduto'),
    path('salvar/', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('flista_produtos/', flista_produtos, name='flista_produtos')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)