# coding=utf-8
from django.db import models
from .recurso import Recurso

"""
Modelo de plan de producción
"""
class PlanProduccion(models.Model):
    recurso = models.OneToOneField(Recurso, on_delete=models.CASCADE, related_name='plan')
    descripcion = models.CharField(max_length=2000, null=True)
