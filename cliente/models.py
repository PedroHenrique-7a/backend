from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=60, unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.telefone} - {self.email}"

    # REGRA DE NEGÓCIO PARA VERIFICAR A SENHA DO CLIENTE
    def verificar_senha(self, senha):
        print(f"Comparando senha fornecida: {senha} com a armazenada: {self.senha}")
        return check_password(senha, self.senha)
