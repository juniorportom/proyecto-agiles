from django.db import models
from .etiqueta import Etiqueta
from datetime import datetime


class Tipo(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'tipos'


# Create your models here.
class Recurso(models.Model):
    FASE_TYPES = (
        ('A', 'Pre-Producción'),
        ('B', 'Producción'),
        ('C', 'Pos-Producción'),
        ('D', 'Control calidad'),
        ('E', 'Cierre proyecto'),
        ('F', 'Sistematización y resguardo')
    )
    nombre = models.CharField(max_length=200)
    proyecto = models.CharField(max_length=200)
    fase = models.CharField(max_length=1, choices=FASE_TYPES)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=datetime.now, blank=True)
    ruta_compartida = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "recurso"
        verbose_name_plural = "recursos"
        ordering = ['-fecha_creacion']
