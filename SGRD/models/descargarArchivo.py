from django.db import models
from datetime import datetime
from django.utils import timezone
from .archivo import Archivo


# Create your models here.
class DescargarArchivo(models.Model):
    fecha_descarga = models.DateField(default=datetime.now, blank=True)
    hora_descarga = models.TimeField(default=timezone.now)
    archivo = models.OneToOneField(Archivo, on_delete=models.CASCADE, blank=True, related_name='descarga')

    def __str__(self):
        return 'Descarga de ' + self.archivo.nombre
