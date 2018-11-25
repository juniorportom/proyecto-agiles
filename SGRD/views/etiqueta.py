# coding=utf-8
from django.shortcuts import render

from SGRD.models.recurso import Recurso
from SGRD.models.etiqueta import Etiqueta
from SGRD.models.clip import Clip
from SGRD.forms.etiqueta import EtiquetaForm
from django.http import HttpResponseRedirect


"""
Vista de etiquetas
"""
def manage_tags(request):
    tags = Etiqueta.objects.all()
    newTag_form = EtiquetaForm(request.POST or None)
    if newTag_form.is_valid():
        Etiqueta.objects.create(**newTag_form.cleaned_data)
        return HttpResponseRedirect('/tags')

    context = {
        'tags': tags,
        'form': newTag_form
    }
    return render(request, 'SGRD/manage_tags.html', context)

"""
Vista de eliminación de etiqueta
"""
def delete_tag(request, id_tag):
    tag = Etiqueta.objects.get(id=id_tag)
    if request.method == 'POST':
        tag.delete()
        return HttpResponseRedirect('/tags')

    context = {
        'tag': tag
    }

    return render(request, 'confirmation/delete_tag.html', context)

"""
Vista para quitar la relación de una etiqueta a un recurso
"""
def remove_tag(request, pk, id_tag):
    recurso = Recurso.objects.get(id=pk)
    tag = Etiqueta.objects.get(id=id_tag)
    if recurso and tag:
        recurso.etiquetas.remove(tag)

    return HttpResponseRedirect('/recurso/' + str(pk))

"""
Vista para agregar la relación de una etiqueta a un recurso
"""
def add_tag(request, pk):
    recurso = Recurso.objects.get(id=pk)
    if recurso and request.method == 'POST':
        tags = request.POST.getlist('addTags')
        recurso.etiquetas.add(*tags)

    return HttpResponseRedirect('/recurso/' + str(pk))

"""
Vista para quitar la relación de una etiqueta a un clip
"""
def remove_tag_clip(request, pk, id_tag, id_archivo):
    clip = Clip.objects.get(id=pk)
    tag = Etiqueta.objects.get(id=id_tag)
    if clip and tag:
        clip.etiquetas.remove(tag)

    return HttpResponseRedirect('/clips/' + str(id_archivo))

"""
Vista para agregar la relación de una etiqueta a un clip
"""
def add_tag_clip(request, pk, id_archivo):
    clip = Clip.objects.get(id=pk)
    if clip and request.method == 'POST':
        tags = request.POST.getlist('addTags')
        clip.etiquetas.add(*tags)

    return HttpResponseRedirect('/clips/'+str(id_archivo))