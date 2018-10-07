from django.contrib import admin
from .models.recurso import Recurso, Tipo
from .models.archivo import Archivo
from .models.planProduccion import PlanProduccion
# Register your models here.
admin.site.register(Recurso)
admin.site.register(Tipo)
admin.site.register(Archivo)
admin.site.register(PlanProduccion)