# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from SGRD.models.clip import Clip


"""
Formulario para un clip
"""
class ClipForm(forms.ModelForm):
    class Meta:
        model = Clip
        fields = ['nombre', 'inicio', 'final']
        labels = {
            'nombre': _("Nombre"),
            'inicio': _("Tiempo Inicial"),
            'final': _("Tiempo Final"),

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'inicio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo Inicial'}),
            'final': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo Final'}),
        }