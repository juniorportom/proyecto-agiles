# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from SGRD.models.planProduccion import PlanProduccion

"""
Formulario para plan de producción
"""
class PlanProduccionForm(forms.ModelForm):
    class Meta:
        model = PlanProduccion
        fields = ['descripcion']

        labels = {
            'descripcion': _("Descripción"),
        }

        widgets = {
            #'recurso': forms.HiddenInput(),
            #'recurso': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Recurso', 'default':'2'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
        }
