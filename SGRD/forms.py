from django import forms
from django.utils.translation import gettext as _
from .models.recurso import Recurso
from .models.entradaPlan import EntradaPlan
from .models.planProduccion import PlanProduccion
from .models.archivo import Archivo
from .models.clip import Clip

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
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'})
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
        labels={
          'dia': 'Día',
          'descripcion': 'Descripción'
        }


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
