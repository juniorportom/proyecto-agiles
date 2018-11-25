# coding=utf-8
from django.shortcuts import render

from SGRD.models.archivo import Archivo
from SGRD.models.descargarArchivo import DescargarArchivo
from SGRD.forms.descargarArchivo import DescargarArchivoForm
from django.http import HttpResponseRedirect, JsonResponse

import  datetime

"""
Vista de crear una programación de descarga de archivo
"""
def planear_descarga(request, id_archivo, id_recurso):

    form = DescargarArchivoForm(request.POST or None)
    if form.is_valid():
        archivo = Archivo.objects.get(id=id_archivo)
        DescargarArchivo.objects.create(**form.cleaned_data, archivo=archivo)
        return HttpResponseRedirect('/recurso/'+str(id_recurso))

    context = {
        'id_recurso': id_recurso,
        'id_archivo': id_archivo,
        'form': form
    }
    return render(request, 'forms/descargar-archivo-form.html', context)

"""
Vista de editar plan de descarga de archivo
"""
def editar_plan_descarga(request, id_archivo, id_recurso):

    archivo = Archivo.objects.get(id=id_archivo)
    descarga = archivo.descarga

    form = DescargarArchivoForm(request.POST or None, instance=descarga)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/recurso/'+str(id_recurso))

    context = {
        'id_recurso': id_recurso,
        'id_archivo': id_archivo,
        'form': form
    }
    return render(request, 'forms/editar-descargar-archivo-form.html', context)

"""
Vista JSON para verificación de descargas pendientes
"""
def check_for_downloads(request):

    data = {
        'downloads': []
    }
    descargas = DescargarArchivo.objects.all()
    for dl in descargas:
        if dl.fecha_descarga >= datetime.date.today() and dl.hora_descarga <= datetime.datetime.now().time():
            newDL = {'id': dl.archivo.id, 'uri': dl.archivo.get_absolute_url()}
            data['downloads'].append(newDL)
            dl.delete()

    return JsonResponse(data)