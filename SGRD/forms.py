from django import forms
from django.utils.translation import gettext as _
from .models.recurso import Recurso
from .models.entradaPlan import EntradaPlan
from .models.archivo import Archivo

class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nombre', 'proyecto', 'fase', 'tipo', 'fecha_creacion', 'ruta_compartida', 'descripcion']
        labels = {
            'nombre': _("Nombre"),
            'proyecto': _("Proyecto"),
            'fase': _("Fase"),
            'tipo': _("Tipo Recurso"),
            'fecha_creacion': _("Fecha de Producción"),
            'ruta_compartida': _("Ubicación recurso"),
            'descripcion' : _("Descripción")
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'proyecto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Proyecto'}),
            'fase': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Fase'}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo recurso'}),
            'fecha_creacion': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder':'yyyy-MM-dd', 'type': 'date'}),
            'ruta_compartida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación recurso'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrpción'})
        }

class CreateEntradaPlanForm(forms.ModelForm):
    class Meta:
        model = EntradaPlan
        fields = ['dia', 'hora', 'lugar', 'personas', 'equipos', 'descripcion', 'observaciones']
        widgets = {
          'dia': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder':'yyyy-MM-dd', 'type': 'date'}),
          'hora': forms.TimeInput(format=('%H:%M'), attrs={'class': 'form-control','placeholder':'HH:MM', 'type': 'time'}),
          'lugar': forms.TextInput(attrs={'class': 'form-control'}),
          'personas': forms.Textarea(attrs={'class': 'form-control'}),
          'equipos': forms.Textarea(attrs={'class': 'form-control'}),
          'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
          'observaciones': forms.Textarea(attrs={'class': 'form-control'})
        }

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['nombre', 'recurso', 'ruta', 'fecha_creacion']
"""        labels = {
            'nombre': _("Nombre"),
            'recurso': _("Recurso"),
            'ruta': _("Ruta archivo"),
            'fecha_creacion': _("Fecha de creación")
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'recurso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recurso'}),
            'ruta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ruta archivo'}),
            'fecha_creacion': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder':'yyyy-MM-dd', 'type': 'date'})
        }
"""
