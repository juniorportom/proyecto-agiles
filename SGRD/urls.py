from django.urls import path
from SGRD import views
from .views import RecursoCreate, ArchivoCreate

urlpatterns = [
    path('', views.index, name='index'),
    path('create-recurso/', RecursoCreate.as_view(), name='create-recurso'),
    path('create-archivo/', ArchivoCreate.as_view(), name='create-archivo'),
]
