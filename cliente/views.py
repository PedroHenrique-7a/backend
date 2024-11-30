from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


# Create your views here.

def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "rel_cliente.html",{"clientes":clientes})

def Frel(request):
    return render(request, 'rel_cliente.html')

def Fcadcliente(request):
    return render(request, "cad_cliente.html")

def salvar_cli(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    vsenha = request.POST.get("senha")

    senha_criptografada = make_password(vsenha)
    if vnome:
        Cliente.objects.create(nome=vnome, telefone=vtelefone, email=vemail, senha=senha_criptografada)
    return redirect(fcliente)

def exibir_cli(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "update_cli.html", {"cliente": cliente})


def excluir_cli(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect(fcliente)


def logar(request):
    if request.method == 'POST':
        email = request.POST.get("username")
        senha = request.POST.get("password")

        # Verifique se os campos estão preenchidos
        if email and senha:
            # Busca todos os clientes com o e-mail fornecido
            clientes = Cliente.objects.filter(email=email)

            if clientes.exists():
                cliente = clientes.first()  # Pega o primeiro cliente encontrado
                if check_password(senha, cliente.senha):  # Use o check_password para comparar senhas criptografadas
                    # Redireciona para a tela do cliente
                    return redirect('ftelacli')
                else:
                    messages.error(request, 'Senha incorreta.')
                    return redirect('login')
            else:
                messages.error(request, 'E-mail não encontrado.')
                return redirect('login')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('login')

    # Se a requisição for GET, apenas renderize a página de login
    return render(request, 'login.html')

def login(request):
    return render(request, "login.html")

def ftelacli(request):
    return render(request, "ftelacli.html")
