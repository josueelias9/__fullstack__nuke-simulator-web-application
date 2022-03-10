from django.db import models
from django.forms import CharField

# Create your models here.


class Geometria(models.Model):
    nombre = models.CharField(max_length=50, default='')
    coordenadas = models.CharField(max_length=50,default='')