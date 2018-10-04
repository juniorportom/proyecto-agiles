from django.shortcuts import render
from .models.recurso import Recurso
from .models.PlanProduccion import PlanProduccion
from .models.entradaPlan import EntradaPlan
from .forms import CreateEntradaPlanForm, RecursoForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):

    context = {

    }
    return render(request, 'SGRD/index.html', context)

def createEntradaPlan(request, idPlan):

    plan_entrada = PlanProduccion.objects.get(id=idPlan)
    form = CreateEntradaPlanForm(request.POST or None)
    if form.is_valid():
        EntradaPlan.create(**form.cleaned_data, plan=plan_entrada)
        form = CreateEntradaPlanForm()

    context = {
        'planProduccion': plan_entrada,
        'form': form
    }

    return render(request, 'SGRD/index.html', context)

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
