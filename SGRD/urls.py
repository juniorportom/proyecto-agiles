from django.urls import path
from SGRD import views
from .views import RecursoCreate, ArchivoCreate, RecursoListView

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-entrada/', views.createEntradaPlan, name='create-entrada'),
    path('crear-recurso/', RecursoCreate.as_view(), name='create-recurso'),
    path('crear-archivo/', ArchivoCreate.as_view(), name='create-archivo'),
    path('recursos/', RecursoListView.as_view(), name='recursos'),
]
