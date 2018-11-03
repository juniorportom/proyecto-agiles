from django.db import models
from .archivo import Archivo


class Clip(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    inicio = models.IntegerField(default=0)
    final = models.IntegerField(default=0)
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE, related_name='clips')

    def __str__(self):
        return self.nombre
