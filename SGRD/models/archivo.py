from django.db import models
from datetime import datetime
from .recurso import Recurso

class Archivo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    ruta = models.FileField(upload_to='archivos_recursos/')
    fecha_creacion = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        # return self.ruta.url
        return 'https://s3.amazonaws.com/agiles-media/' + str(self.ruta.name)
