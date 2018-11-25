from django.db import models

"""
Modelo de tipo de recurso
"""
class Tipo(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'tipos'
