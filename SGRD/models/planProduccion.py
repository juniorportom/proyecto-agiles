from django.db import models
from .recurso import Recurso

class PlanProduccion(models.Model):
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE, related_name='plan')
