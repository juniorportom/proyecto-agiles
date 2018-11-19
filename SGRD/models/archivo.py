from django.db import models
from datetime import datetime
from .recurso import Recurso
from .descargarArchivo import DescargarArchivo


class Archivo(models.Model):
    nombre = models.CharField(max_length=200)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    ruta = models.FileField(upload_to='archivos_recursos/')
    fecha_creacion = models.DateField(default=datetime.now, blank=True)
    descarga_archivo = models.OneToOneField(DescargarArchivo, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        # return self.ruta.url
        return 'https://s3.amazonaws.com/agiles-media/' + str(self.ruta.name)
