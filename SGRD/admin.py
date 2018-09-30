from django.contrib import admin
from .models.recurso import Recurso, Tipo
# Register your models here.
admin.site.register(Recurso)
admin.site.register(Tipo)