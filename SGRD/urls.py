from django.urls import path
from SGRD import views
from .views import RecursoCreate

urlpatterns = [
    path('', views.index, name='index'),
    path('create-recurso/', RecursoCreate.as_view(), name='create-recurso'),
]
