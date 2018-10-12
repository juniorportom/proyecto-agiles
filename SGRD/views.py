from django.shortcuts import render

from .models.archivo import Archivo
from .models.recurso import Recurso
from .models.planProduccion import PlanProduccion
from .models.entradaPlan import EntradaPlan
from .forms import CreateEntradaPlanForm, RecursoForm, ArchivoForm, PlanProduccionForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
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
    plan_entrada = recurso.plan.get()

    form = CreateEntradaPlanForm(request.POST or None)
    if form.is_valid():
        EntradaPlan.objects.create(**form.cleaned_data, plan=plan_entrada)
        return HttpResponseRedirect('/planProduccion/'+str(recurso.id))

    context = {
        'recurso': recurso,
        'planProduccion': plan_entrada,
        'form': form
    }

    return render(request, 'forms/createEntradaPlanForm.html', context)

def viewPlanProduccion(request, idRecurso):
    recurso = Recurso.objects.get(id=idRecurso)
    plan = recurso.plan.get()
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
    success_url = reverse_lazy('index')


class RecursoListView(ListView):
    model = Recurso
    template_name = 'forms/recurso_list.html'
    paginate_by = 50


class CrearPlanProduccion(CreateView):
    model = PlanProduccion
    form_class = PlanProduccionForm
    template_name = 'forms/crear_plan.html'
    success_url = reverse_lazy('index')


def EditarPlanProduccion(request, idPlan):
    plan = PlanProduccion.objects.get(id=idPlan)

    if request.method == 'POST':
        form_plan = PlanProduccionForm(request.POST, instance=plan)

        if form_plan.is_valid():
            form_plan.save()
            return HttpResponseRedirect('/')

    else:
        form_plan = PlanProduccionForm(instance=plan)

    context = {'form_plan': form_plan}

    return render(request, 'forms/editarPlanProduccion.html', context)