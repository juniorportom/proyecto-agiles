# coding=utf-8
from django.shortcuts import render

from SGRD.models.planProduccion import PlanProduccion
from SGRD.forms.planProduccion import PlanProduccionForm
from SGRD.models.recurso import Recurso
from SGRD.models.entradaPlan import EntradaPlan
from SGRD.forms.entradaPlan import CreateEntradaPlanForm
from django.http import HttpResponseRedirect, StreamingHttpResponse, HttpResponse

import io
import xlsxwriter


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

    return HttpResponseRedirect('/recursos/')

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
Vista de eliminar entrada de plan de producción
"""
def delete_entrada(request, idEntrada):

    entrada = EntradaPlan.objects.get(id=idEntrada)
    recurso = entrada.plan.recurso.id

    entrada.delete()
    return HttpResponse(status=200)