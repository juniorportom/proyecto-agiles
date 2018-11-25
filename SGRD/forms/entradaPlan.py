# coding=utf-8
from django import forms
from SGRD.models.entradaPlan import EntradaPlan

"""
Formulario para entrada de plan de producción
"""
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
