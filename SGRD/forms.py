# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from .models.recurso import Recurso
from .models.entradaPlan import EntradaPlan
from .models.planProduccion import PlanProduccion
from .models.archivo import Archivo
from .models.clip import Clip
from .models.tipo import Tipo
from .models.etiqueta import Etiqueta
from .models.descargarArchivo import DescargarArchivo

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

"""
Formulario para plan de producción
"""
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
