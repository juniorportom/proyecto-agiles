# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from SGRD.models.etiqueta import Etiqueta


"""
Formulario para una etiqueta
"""
class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = '__all__'
        labels = {
            'nombre': _("Nombre"),
            'color': _("Color")
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'color': forms.TextInput(attrs={'type': 'color', 'placeholder': '#79ADDC'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Etiqueta.objects.filter(nombre__iexact=nombre).exists():
            raise ValidationError(_('Ya existe una etiqueta con el mismo nombre'), code='invalid')
        return nombre
