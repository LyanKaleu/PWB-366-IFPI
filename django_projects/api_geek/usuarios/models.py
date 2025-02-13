from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('VENDEDOR', 'Vendedor'),
        ('CLIENTE', 'Cliente'),
    ]
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default='CLIENTE',
    )

    def __str__(self):
        return self.username
