# coding=utf-8
from django.shortcuts import render

from SGRD.models.archivo import Archivo
from SGRD.models.etiqueta import Etiqueta
from SGRD.models.clip import Clip
from SGRD.forms.clip import ClipForm
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


"""
Vista de detalle de clips relacionados a un archivo
"""
def archivoClips(request, idArchivo):
    archivo = Archivo.objects.get(id=idArchivo)
    clips = archivo.clips.all()
    otherTags = Etiqueta.objects.all()

    context = {
        'archivo': archivo,
        'clips': clips,
        'otherTags': otherTags
    }
    return render(request, 'SGRD/archivo_clips.html', context)



"""
Vista de crear clip a archivo
"""
class ClipCreate(CreateView):
    model = Clip
    form_class = ClipForm
    template_name = 'forms/clip-form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archivo'] = Archivo.objects.filter(recurso=self.kwargs['id_recurso']).filter(ruta__contains='.mp4')

        return context

    def form_valid(self, form):
        archivo_id = self.request.POST.get('file')
        form.instance.archivo = get_object_or_404(Archivo, id=archivo_id)
        nombre_clip = form.cleaned_data['nombre']
        tiempo_inicio = form.cleaned_data['inicio']
        tiempo_final = form.cleaned_data['final']
        if len(nombre_clip) == 0:
            form.add_error('nombre', 'Campo Nombre obligatorio')
            return self.form_invalid(form)
        if int(tiempo_inicio) >= int(tiempo_final):
            form.add_error('final', 'Tiempo final debe ser mayor al tiempo inicial')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('recurso', kwargs={'pk': self.kwargs['id_recurso']})


"""
Vista de eliminar clip
"""
class ClipDelete(DeleteView):
    model = Clip
    template_name = "confirmation/delete_clip.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy('ver-clips', kwargs={'idArchivo': self.kwargs['idArchivo']})