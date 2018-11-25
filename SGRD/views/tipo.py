# coding=utf-8

from SGRD.models.tipo import Tipo
from django.http import HttpResponseRedirect
from django.contrib import messages


import io, datetime
import xlsxwriter


"""
Vista de crear tipo
"""
def crear_tipo(request):
    if request.method == 'POST':
        nombreTipo = request.POST.get('tiponame')
        tipo = Tipo.objects.filter(nombre=nombreTipo)

        if not tipo:
            tipo = Tipo(nombre=nombreTipo)
            tipo.save()
            messages.success(request, "¡Tipo se registro correctamente!", extra_tags="alert-success")
        else:
            messages.error(request, "¡Tipo ya se encuentra registrado!", extra_tags="alert-danger")

    return HttpResponseRedirect('/crear-recurso')
