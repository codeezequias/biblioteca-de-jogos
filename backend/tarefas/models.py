from django.db import models
from usuarios.models import Usuario


class EventoAcademico(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    nome = models.CharField(max_length=255)
    local = models.TextField()
    data = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ABERTA'
    )
    usuario_responsavel = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='eventos_academicos'
    )

    def __str__(self):
        return self.nome


class EventoCiberseguranca(models.Model):
    CATEGORIA_CHOICES = [
        ('WORKSHOP', 'Workshop'),
        ('PALESTRA', 'Palestra'),
        ('TREINAMENTO', 'Treinamento'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.DateField()
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        default='PALESTRA'
    )
    usuario_responsavel = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='eventos_ciberseguranca'
    )

    def __str__(self):
        return self.titulo

