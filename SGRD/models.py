from django.db import models

# Create your models here.
class Recurso(models.Model):
    name = models.CharField(max_length=200)

class PlanProduccion(models.Model):
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)

class EntradaPlan(models.Model):
    plan = models.ForeignKey(PlanProduccion, on_delete=models.CASCADE)
    dia = models.DateField()
    hora = models.TimeField()
    lugar = models.TextField()
    personas = models.TextField()
    equipos = models.TextField()
    descripcion = models.TextField()
    observaciones = models.TextField()
