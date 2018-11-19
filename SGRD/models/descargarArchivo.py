from django.db import models
from datetime import datetime
from .archivo import Archivo
from django.utils import timezone


# Create your models here.
class DescargarArchivo(models.Model):
    archivo = models.OneToOneField(Archivo, on_delete=models.CASCADE)
    fecha_descarga = models.DateField(default=datetime.now, blank=True)
    hora_descarga = models.TimeField(default=timezone.now)
