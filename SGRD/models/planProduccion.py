from django.db import models
from .recurso import Recurso

class PlanProduccion(models.Model):
    recurso = models.OneToOneField(Recurso, on_delete=models.CASCADE, related_name='plan')
    descripcion = models.CharField(max_length=2000, null=True)
