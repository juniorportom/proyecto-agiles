from django.db import models
from .planProduccion import PlanProduccion

class EntradaPlan(models.Model):
    plan = models.ForeignKey(PlanProduccion, on_delete=models.CASCADE, related_name='entradas')
    dia = models.DateField()
    hora = models.TimeField()
    lugar = models.TextField()
    personas = models.TextField()
    equipos = models.TextField()
    descripcion = models.TextField()
    observaciones = models.TextField()
