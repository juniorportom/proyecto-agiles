from django.db import models

class EntradaPlanModel(models.Model):
    #plan = models.ForeignKey(PlanProduccion, on_delete=models.CASCADE)
    dia = models.DateField()
    hora = models.TimeField()
    lugar = models.TextField()
    personas = models.TextField()
    equipos = models.TextField()
    descripcion = models.TextField()
    observaciones = models.TextField()
