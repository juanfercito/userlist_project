from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    identificacion = models.IntegerField()
    email = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
