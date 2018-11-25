from django.contrib import admin
from .models.recurso import Recurso
from .models.archivo import Archivo
from .models.planProduccion import PlanProduccion
from .models.entradaPlan import EntradaPlan
from .models.etiqueta import Etiqueta
from .models.tipo import Tipo
from .models.clip import Clip
from .models.descargarArchivo import DescargarArchivo
# Register your models here.
admin.site.register(Recurso)
admin.site.register(Tipo)
admin.site.register(Archivo)
admin.site.register(PlanProduccion)
admin.site.register(EntradaPlan)
admin.site.register(Etiqueta)
admin.site.register(Clip)
admin.site.register(DescargarArchivo)