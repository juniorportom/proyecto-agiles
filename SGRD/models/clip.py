from django.db import models
from .archivo import Archivo
from .etiqueta import Etiqueta

"""
Modelo de clip
"""
class Clip(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    inicio = models.IntegerField(default=0)
    final = models.IntegerField(default=0)
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE, related_name='clips')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return self.nombre
