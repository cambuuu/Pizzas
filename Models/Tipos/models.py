from django.utils import timezone

from django.db import models

class Tipos(models.Model):
    nombre = models.CharField(max_length=100)
    direccion  = models.CharField(max_length=75)
    fono = models.CharField(max_length=12)
    email = models.CharField(max_length=75)
    masa = models.CharField(max_length=75)
    salsa = models.CharField(max_length=75)
    queso = models.CharField(max_length=75)
    ingrediente1 = models.CharField(max_length=75)
    ingrediente2 = models.CharField(max_length=75)
    ingrediente3 = models.CharField(max_length=75)
    bebida = models.CharField(max_length=75)
    observacion = models.CharField(max_length=75)

class Usuario(models.Model):
    nombre = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    correo = models.CharField(max_length=60)
    fono = models.CharField(max_length=15)
    contrasena= models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title