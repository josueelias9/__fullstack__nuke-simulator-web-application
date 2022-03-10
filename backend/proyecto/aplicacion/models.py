from django.db import models
from django.forms import CharField

# Create your models here.


class Geometria(models.Model):
    info = models.CharField(max_length=50, default='')
    color = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=50, default='')
    coordinates = models.TextField(default='')
    
    