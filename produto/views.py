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
    vcategoria= request.POST.get('categoria')

    if vnome:
        Produto.objects.create(
            nome=vnome,
            descricao=vdescricao,
            preco=vpreco,
            quantidade=vquantidade,
            imagem=vimagem,
            categoria=vcategoria)
    return redirect('produto:fprodutos')

def editar(request, id):
    produto= Produto.objects.get(id=id)
    return render(request, 'update.html', {'produto', produto})


def excluir(request, id):
    produto= Produto.objects.get(id=id)
    produto.delete()
    return redirect('produto:fprodutos')

def update(request, id):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    produto= Produto.objects.get(id=id)
    produto.nome= vnome
    produto.descricao= vdescricao
    produto.preco= vpreco
    produto.quantidade= vquantidade
    produto.save()
    return redirect(fprodutos)


def flista_produtos(request):
    categoria= request.GET.get('categoria')
    if categoria:
        produtos= Produto.objects.filter(categoria=categoria)
    else:
        produtos=Produto.objects.all()

    return render(request, 'flista_produtos.html', {'produtos': produtos})