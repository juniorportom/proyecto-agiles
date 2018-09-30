from django.shortcuts import render
from .models.recurso import Recurso
from .models.PlanProduccion import PlanProduccion
from .models.entradaPlan import EntradaPlan
from .forms import CreateEntradaPlanForm

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
