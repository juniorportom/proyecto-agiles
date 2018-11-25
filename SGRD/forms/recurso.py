# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from SGRD.models.recurso import Recurso

"""
Formulario para un recurso
"""
class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nombre', 'proyecto', 'fase', 'tipo', 'inicio_produccion', 'fin_elaboracion_recurso', 'fecha_publicacion', 'descripcion']
        labels = {
            'nombre': _("Nombre"),
            'proyecto': _("Proyecto"),
            'fase': _("Fase"),
            'tipo': _("Tipo Recurso"),
            'inicio_produccion': _("Fecha de inicio producción"),
            'fin_elaboracion_recurso': _("Fecha final de elaboración"),
            'fecha_publicacion': _("Fecha de publicación"),
            'descripcion' : _("Descripción")
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'proyecto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Proyecto'}),
            'fase': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Fase'}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo recurso'}),
            'inicio_produccion': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder':'yyyy-MM-dd', 'type': 'date'}),
            'fin_elaboracion_recurso': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd', 'type': 'date'}),
            'fecha_publicacion': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'})
        }