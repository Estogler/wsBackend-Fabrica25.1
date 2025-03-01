from django.db import models

class Usuario(models.Model):
    Usuario_nome = models.CharField(max_length=50)
    Usuario_moeda_atual = models.CharField(max_length=200)
    Usuario_moeda_para_conversao = models.CharField(max_length=200)
    Usuario_moeda_convertida = models.CharField(max_length=200)

    def __str__(self):
        return f'nome: {self.Usuario_nome}, moeda atual: {self.Usuario_moeda_atual}, moeda para conversao: {self.Usuario_moeda_para_conversao}, moeda convertida: {self.Usuario_moeda_convertida}'
