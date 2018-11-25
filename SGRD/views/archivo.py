# coding=utf-8

from SGRD.models.archivo import Archivo
from SGRD.models.recurso import Recurso
from SGRD.forms.archivo import ArchivoForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

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
