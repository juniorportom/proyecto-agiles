# coding=utf-8
from django.shortcuts import render

from SGRD.models.archivo import Archivo
from SGRD.models.recurso import Recurso
from SGRD.models.etiqueta import Etiqueta
from SGRD.models.tipo import Tipo
from SGRD.models.clip import Clip
from SGRD.models.descargarArchivo import DescargarArchivo
from SGRD.forms.recurso import RecursoForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


"""
Vista de crear recurso
"""
class RecursoCreate(CreateView):
    model = Recurso
    form_class = RecursoForm
    template_name = 'forms/recurso-form.html'
    success_url = reverse_lazy('recursos')


"""
Vista de recursos
"""
class RecursoListView(ListView):
    model = Recurso
    template_name = 'SGRD/recurso_list.html'
    paginate_by = 50


"""
Vista de detalle de recurso
"""
class RecursoDetailView(DetailView):
    model = Recurso
    template_name = 'SGRD/recurso_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archivos'] = Archivo.objects.filter(recurso=self.object)
        context['tags'] = self.object.etiquetas.all()
        context['otherTags'] = Etiqueta.objects.exclude(id__in=context['tags'])
        context['descargas'] = DescargarArchivo.objects.all()
        print(self.object.id)
        if not context['archivos']:
            context['archivos'] = ''

        try:
            if not self.object.plan:
                context['hay_plan'] = False
            else:
                context['hay_plan'] = True
        except:
            context['hay_plan'] = False

        context['tipo_video'] = self.object.tipo.nombre == "Video"
        context['produccion_terminada'] = str(self.object.fase) in ['C', 'D', 'E', 'F']
        context['archivos_terminados'] = Archivo.objects.filter(recurso=self.object, recurso__archivo__terminado__exact='True')
        context['archivos_no_terminados'] = Archivo.objects.filter(recurso=self.object, recurso__archivo__terminado__exact='False')
        return context

"""
Vista de búsqueda de recursos
"""
def recursoBusqueda(request):
    tags = request.GET.getlist('tags')
    type = request.GET.get('types', -1)

    type = int(type)

    recursos = Recurso.objects.all()
    clips = Clip.objects.all()

    if type != -1:
        recursos = recursos.filter(tipo=type)

    for pk in tags:
        recursos = recursos.filter(etiquetas__in=pk)
        clips = clips.filter(etiquetas__in=pk)

    all_tags = Etiqueta.objects.all()
    all_types = Tipo.objects.all()

    context = {
        'searchParams': {
            'type': type,
            'tags': tags,
        },
        'types': all_types,
        'tags': all_tags,
        'recursos': recursos,
        'clips': clips
    }
    return render(request, 'SGRD/busqueda.html', context)