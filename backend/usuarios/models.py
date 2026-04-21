from django.db import models

class Usuario(models.Model):
     nome = models.CharField()
     email = models.EmailField()
     ativo = models.BooleanField(True)
     data_criacao = models.DateTimeField(auto_now_add=True)
     
     
     def __str__(self):
        return self.nome




