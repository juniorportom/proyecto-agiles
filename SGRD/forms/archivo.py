# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from SGRD.models.archivo import Archivo


"""
Formulario para  un archivo
"""
class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['nombre', 'ruta', 'fecha_creacion']
        labels = {
            'nombre': _("Nombre"),
            'ruta': _("Ruta archivo"),
            'fecha_creacion': _("Fecha de creación")
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'ruta': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Archivo'}),
            'fecha_creacion': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder':'yyyy-MM-dd', 'type': 'date'})
        }
