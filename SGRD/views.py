from django.shortcuts import render

from .models.archivo import Archivo
from .models.recurso import Recurso
from .models.planProduccion import PlanProduccion
from .models.entradaPlan import EntradaPlan
from .models.etiqueta import Etiqueta
from .models.tipo import Tipo
from .models.clip import Clip
from .forms import CreateEntradaPlanForm, RecursoForm, ArchivoForm, PlanProduccionForm, ClipForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import date

# Create your views here.
def index(request):

    context = {

    }
    return render(request, 'SGRD/index.html', context)

def createEntradaPlan(request, idRecurso):
    plan_entrada = None
    form = None

    recurso = Recurso.objects.get(id=idRecurso)
    plan_entrada = recurso.plan

    form = CreateEntradaPlanForm(request.POST or None)
    if form.is_valid():
        EntradaPlan.objects.create(**form.cleaned_data, plan=plan_entrada)
        return verPlanProduccion(request, recurso.id)

    context = {
        'recurso': recurso,
        'planProduccion': plan_entrada,
        'form': form
    }

    return render(request, 'forms/createEntradaPlanForm.html', context)

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

def sortEntradasPlan(entradas):
    dias = {}
    for e in entradas:
        dia = e.dia
        if dia in dias:
            dias[dia].append(e)
        else:
            dias[dia] = [e]
    return dias


class RecursoCreate(CreateView):
    model = Recurso
    form_class = RecursoForm
    template_name = 'forms/recurso-form.html'
    success_url = reverse_lazy('recursos')


class ArchivoCreate(CreateView):
    model = Archivo
    form_class = ArchivoForm
    template_name = 'forms/archivo-form.html'
    success_url = reverse_lazy('recursos')

    def form_valid(self, form):
        form.instance.recurso = get_object_or_404(Recurso, id=self.kwargs['id_recurso'])
        return super().form_valid(form)


class RecursoListView(ListView):
    model = Recurso
    template_name = 'SGRD/recurso_list.html'
    paginate_by = 50


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

    return HttpResponseRedirect('/recursos/')

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


class RecursoDetailView(DetailView):
    model = Recurso
    template_name = 'SGRD/recurso_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archivos'] = Archivo.objects.filter(recurso=self.object)
        context['tags'] = self.object.etiquetas.all()
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
        return context

def archivoClips(request, idArchivo):
    archivo = Archivo.objects.get(id=idArchivo)
    clips = archivo.clips.all()

    context = {
        'archivo': archivo,
        'clips': clips,
    }
    return render(request, 'SGRD/recurso_detail.html', context)


def recursoBusqueda(request):
    tags = request.GET.getlist('tags')
    type = request.GET.get('types', -1)

    type = int(type)

    recursos = Recurso.objects.all()

    if type != -1:
        recursos = recursos.filter(tipo=type)

    for pk in tags:
        recursos = recursos.filter(etiquetas__in=pk)

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
    }
    return render(request, 'SGRD/busqueda.html', context)


class ClipCreate(CreateView):
    model = Clip
    form_class = ClipForm
    template_name = 'forms/clip-form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archivo'] = Archivo.objects.filter(recurso=self.kwargs['id_recurso'])

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
        return reverse_lazy('recurso', kwargs = {'pk': self.kwargs['id_recurso']})
