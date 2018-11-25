# coding=utf-8
from django import forms
from SGRD.models.descargarArchivo import DescargarArchivo


"""
Formulario para una descarga de archivo
"""
class DescargarArchivoForm(forms.ModelForm):
    class Meta:
        model = DescargarArchivo
        fields = ['fecha_descarga', 'hora_descarga']
        widgets = {
          'fecha_descarga': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder':'yyyy-MM-dd', 'type': 'date'}),
          'hora_descarga': forms.TimeInput(format=('%H:%M'), attrs={'class': 'form-control','placeholder':'HH:MM', 'type': 'time'})
        }
        labels={
          'fecha_descarga': 'Fecha descarga',
          'hora_descarga': 'Hora descarga'
        }
