from django.contrib import admin
from .models.recurso import Recurso, Tipo
from .models.archivo import Archivo
from .models.planProduccion import PlanProduccion
from .models.entradaPlan import EntradaPlan
from .models.etiqueta import Etiqueta
# Register your models here.
admin.site.register(Recurso)
admin.site.register(Tipo)
admin.site.register(Archivo)
admin.site.register(PlanProduccion)
admin.site.register(EntradaPlan)
admin.site.register(Etiqueta)
