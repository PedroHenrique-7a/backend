from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.shortcuts import render, redirect

from .models import Produto

# Create your views here.
def fprodutos(request):
    produtos= Produto.objects.all()
    return render(request, "rel_produto.html", {"produtos":produtos})

def fcadproduto(request):
    return render(request, "cad_produto.html")

def salvar(request):
    vnome= request.POST.get("nome")
    vdescricao= request.POST.get("descricao")
    vpreco= request.POST.get("preco")
    vquantidade= request.POST.get("quantidade")
    vimagem= request.FILES.get('imagem')

    if vnome:
        Produto.objects.create(
            nome=vnome,
            descricao=vdescricao,
            preco=vpreco,
            quantidade=vquantidade,
            imagem=vimagem)
    return redirect(fproduto)

def editar(request, id):
    produto= Produtos.objects.get(id=id)
    return render(request, 'update', {'produto', produto})


def excluir(request, id):
    produto= Produto.objects.get(id=id)
    produto.delete()
    return redirect(fproduto)

def update(request, id):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    produto= produto.objects.get(id=id)
    produto.nome= vnome
    produto.descricao= vdescricao
    produto.preco= vpreco
    produto.quantidade= vquantidade
    produto.save()
    return redirect(fproduto)
# Excluir produto
def excluir(request, id):
    produto = get_object_or_404(Produtos, id=id)
    produto.delete()
    return redirect('fproduto')  # Redireciona para o relatório de produtos

