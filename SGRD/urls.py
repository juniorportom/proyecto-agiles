from django.urls import path
from SGRD import views
from .views import RecursoCreate, ArchivoCreate, RecursoListView

urlpatterns = [
    path('', views.index, name='index'),
    path('planProduccion/<int:idRecurso>', views.viewPlanProduccion, name='view-plan'),
    path('create-entrada/<int:idRecurso>', views.createEntradaPlan, name='create-entrada'),
    path('create-recurso/', RecursoCreate.as_view(), name='create-recurso'),
    path('create-archivo/', ArchivoCreate.as_view(), name='create-archivo'),
    path('recursos/', RecursoListView.as_view(), name='recursos'),
]
