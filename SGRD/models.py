# coding=utf-8
from django.db import models

"""
Importación de los modelos de la carpeta models
"""
# Import your models here.
from .models.entradaPlan import EntradaPlan
from .models.tipo import Tipo
from .models.recurso import Recurso
from .models.archivo import Archivo
from .models.planProduccion import PlanProduccion
from .models.etiqueta import Etiqueta
from .models.clip import Clip
from .models.descargarArchivo import DescargarArchivo
