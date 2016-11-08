from __future__ import unicode_literals

from django.db import models
from diputados.models import Diputado


# Create your models here.

class Iniciativa(models.Model):
    num = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    turno = models.DateTimeField()
    comision = models.CharField(max_length=200)
    resolutivos = models.CharField()
    enlace = models.URLField()
    diputado = models.ForeignKey(Diputado,null=True,blank=True, on_delete=models.CASCADE)
