from django.db import models

"""
Modelo de etiqueta
"""
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200)
    color = models.CharField(max_length=7, default='#79ADDC')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'etiquetas'
