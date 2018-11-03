from django.db import models
from datetime import datetime
from .recurso import Recurso

class Archivo(models.Model):
    nombre = models.CharField(max_length=200)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    ruta = models.FileField(upload_to='archivos_recursos/')
    fecha_creacion = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        # return self.ruta.url
        return 'https://storages.backends.s3boto3.S3Boto3Storage/agiles-media/' + str(self.ruta.name)
