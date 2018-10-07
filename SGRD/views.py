from django.shortcuts import render

from .models.archivo import Archivo
from .models.recurso import Recurso
from .models.planProduccion import PlanProduccion
from .models.entradaPlan import EntradaPlan
from .forms import CreateEntradaPlanForm, RecursoForm, ArchivoForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):

    context = {

    }
    return render(request, 'SGRD/index.html', context)

def createEntradaPlan(request):

    idPlan = 1
    error = False
    plan_entrada = None
    form = None

    plan_entrada = PlanProduccion.objects.all()

    if (len(plan_entrada) > 0):
        plan_entrada = plan_entrada[0]
        form = CreateEntradaPlanForm(request.POST or None)
        if form.is_valid():
            EntradaPlan.create(**form.cleaned_data, plan=plan_entrada)
            form = CreateEntradaPlanForm()
    else:
        error = True

    context = {
        'error': error,
        'planProduccion': plan_entrada,
        'form': form
    }

    return render(request, 'forms/createEntradaPlanForm.html', context)

def viewPlanProduccion(request, idPlan):
    plan = PlanProduccion.objects.get(id=idPlan)
    entradas = plan.entradas.all()

    context = {
        'plan': plan,
        'entradas': entradas
    }

    return render(request, 'SGRD/planProduccion.html', context)

class RecursoCreate(CreateView):
    model = Recurso
    form_class = RecursoForm
    template_name = 'forms/recurso-form.html'
    success_url = reverse_lazy('index')

class ArchivoCreate(CreateView):
    model = Archivo
    form_class = ArchivoForm
    template_name = 'forms/archivo-form.html'
    success_url = reverse_lazy('index')
