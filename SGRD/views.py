# coding=utf-8
from django.shortcuts import render

from .models.archivo import Archivo
from .models.recurso import Recurso
from .models.planProduccion import PlanProduccion
from .models.entradaPlan import EntradaPlan
from .models.etiqueta import Etiqueta
from .models.tipo import Tipo
from .models.clip import Clip
from .models.descargarArchivo import DescargarArchivo
from .forms.recurso import RecursoForm
from .forms.entradaPlan import CreateEntradaPlanForm
from .forms.archivo import ArchivoForm
from .forms.planProduccion import PlanProduccionForm
from .forms.clip import ClipForm
from .forms.etiqueta import EtiquetaForm
from .forms.descargarArchivo import DescargarArchivoForm
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, StreamingHttpResponse, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages


import io, datetime
import xlsxwriter

"""
Vista principal: Listado de archivos y busqueda
"""
def index(request):
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
            'isSearch': len(tags) != 0 or type != -1,
            'type': type,
            'tags': tags,
        },
        'types': all_types,
        'tags': all_tags,
        'recursos': recursos,
        'clips': clips
    }
    return render(request, 'SGRD/index.html', context)

"""
Vista de crear entrada de plan de producción
"""
def createEntradaPlan(request, idRecurso):
    plan_entrada = None
    form = None

    recurso = Recurso.objects.get(id=idRecurso)
    plan_entrada = recurso.plan

    form = CreateEntradaPlanForm(request.POST or None)
    if form.is_valid():
        EntradaPlan.objects.create(**form.cleaned_data, plan=plan_entrada)
        return HttpResponseRedirect('/ver-plan-produccion/' + str(recurso.id))

    context = {
        'recurso': recurso,
        'planProduccion': plan_entrada,
        'form': form
    }

    return render(request, 'forms/createEntradaPlanForm.html', context)

"""
Vista de editar entrada de plan de producción
"""
def editarEntradaPlan(request, idEntrada):
    plan_entrada = None
    form = None

    entrada = EntradaPlan.objects.get(id=idEntrada)
    recurso = entrada.plan.recurso

    form = CreateEntradaPlanForm(request.POST or None, instance=entrada)
    if form.is_valid():
        form.save()
        return verPlanProduccion(request, recurso.id)

    context = {
        'entrada': entrada,
        'form': form,
        'recurso': recurso
    }

    return render(request, 'forms/editarEntradaPlanForm.html', context)

"""
Vista de ver plan de producción
"""
def verPlanProduccion(request, idRecurso):
    recurso = Recurso.objects.get(id=idRecurso)
    plan = recurso.plan
    entradas = plan.entradas.all()
    planDescripcion = plan.descripcion

    entradas = sortEntradasPlan(list(entradas))

    context = {
        'recurso': recurso,
        'plan': plan,
        'entradas': entradas,
        'planDescripcion': planDescripcion
    }

    return render(request, 'SGRD/planProduccion.html', context)

"""
Vista de exportar plan de producción
"""
def exportarPlanProduccion(request, idRecurso):
    recurso = Recurso.objects.get(id=idRecurso)
    plan = recurso.plan
    entradas = list(plan.entradas.all().values())

    output = io.BytesIO()

    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    headers = list(entradas[0])

    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    for row_num, entrada in enumerate(entradas):
        entrada = list(entrada.values())
        for col_num in range(len(entrada)):
            worksheet.write(row_num + 1, col_num, str(entrada[col_num]))

    workbook.close()

    output.seek(0)

    filename = 'plan_produccion.xlsx'
    response = StreamingHttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response

"""
Función para ordenar entradas de plan de producción
"""
def sortEntradasPlan(entradas):
    dias = {}
    for e in entradas:
        dia = e.dia
        if dia in dias:
            dias[dia].append(e)
        else:
            dias[dia] = [e]
    return dias

"""
Vista de crear recurso
"""
class RecursoCreate(CreateView):
    model = Recurso
    form_class = RecursoForm
    template_name = 'forms/recurso-form.html'
    success_url = reverse_lazy('index')

"""
Vista de crear entrada de plan de producción
"""
class ArchivoCreate(CreateView):
    model = Archivo
    form_class = ArchivoForm
    template_name = 'forms/archivo-form.html'

    def form_valid(self, form):
        form.instance.recurso = get_object_or_404(Recurso, id=self.kwargs['id_recurso'])
        form.instance.terminado = self.kwargs['terminado'] == 1
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('recurso', kwargs={'pk': self.kwargs['id_recurso']})

    def get_context_data(self, **kwargs):
        context = super(ArchivoCreate, self).get_context_data(**kwargs)
        context['terminado'] = self.kwargs['terminado'] == 1
        return context

"""
Vista de recursos
"""
class RecursoListView(ListView):
    model = Recurso
    template_name = 'SGRD/recurso_list.html'
    paginate_by = 50

"""
Vista de crear plan de producción
"""
def crearPlanProduccion(request, idRecurso):
    plan_entrada = None
    form = None

    recurso = Recurso.objects.get(id=idRecurso)
    descripcion = PlanProduccion.descripcion
    recurso_id = PlanProduccion.recurso_id

    form = PlanProduccionForm(request.POST or None)
    if recurso_id != '':
        if form.is_valid():
            PlanProduccion.objects.create(**form.cleaned_data, recurso=recurso)
            return verPlanProduccion(request, recurso.id)

        context = {
            'recurso': recurso,
            'descripcion': descripcion,
            'form': form
        }

        return render(request, 'forms/crear_plan.html', context)

    return HttpResponseRedirect('/recurso/'+str(idRecurso))

"""
Vista de editar plan de producción
"""
def EditarPlanProduccion(request, idRecurso):
    try:
        recurso = Recurso.objects.get(id=idRecurso)
        plan = recurso.plan
        form_plan = PlanProduccionForm(request.POST or None, instance=plan)

        if form_plan.is_valid():
            form_plan.save()
            return verPlanProduccion(request, recurso.id)

        context = {
            'form_plan': form_plan,
            'error': False
        }

        return render(request, 'forms/editarPlanProduccion.html', context)

    except:
        context = {
            'form_plan': None,
            'error': True
        }

        return render(request, 'forms/editarPlanProduccion.html', context)

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

"""
Vista de eliminar un plan de producción
"""
def delete_plan(request, idPlan):

    plan = PlanProduccion.objects.get(recurso_id=idPlan)
    if request.method == 'POST':
        plan.delete()
        return HttpResponseRedirect('/recurso/'+str(idPlan))

    context = {
        'plan': plan
    }

    return render(request, 'confirmation/delete_plan.html', context)

"""
Vista de eliminar entrada de plan de producción
"""
def delete_entrada(request, idEntrada):

    entrada = EntradaPlan.objects.get(id=idEntrada)
    recurso = entrada.plan.recurso.id

    entrada.delete()
    return HttpResponse(status=200)

"""
Vista de eliminar clip
"""
class ClipDelete(DeleteView):
    model = Clip
    template_name = "confirmation/delete_clip.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy('ver-clips', kwargs={'idArchivo': self.kwargs['idArchivo']})

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
