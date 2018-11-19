from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class DescargarArchivo(models.Model):
    fecha_descarga = models.DateField(default=datetime.now, blank=True)
    hora_descarga = models.TimeField(default=timezone.now)
