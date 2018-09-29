from django import forms
from .models.recurso import Recurso


class recursoForm(forms.ModelForm):
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

