# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from SGRD.models.tipo import Tipo


"""
Formulario para un tipo
"""
class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre']
        labels = {
            'nombre': _("Nombre")
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
        }
