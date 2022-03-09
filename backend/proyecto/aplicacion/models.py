from django.db import models
from django.forms import CharField

# Create your models here.


class Geometria(models.Model):
    nombre = CharField(max_length=50)
    coordenadas = CharField(max_length=50)