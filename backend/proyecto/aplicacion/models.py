from django.db import models
from django.forms import CharField

# Create your models here.


class Geometria(models.Model):
    class_info = models.CharField(max_length=50, default='')
    class_color = models.CharField(max_length=50, default='')
    class_type = models.CharField(max_length=50, default='Point')
    class_coordinates = models.TextField(default='')
    class_strokeWeight = models.IntegerField(default=0)
    
    