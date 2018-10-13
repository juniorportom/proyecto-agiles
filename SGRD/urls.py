from django.urls import path
from SGRD import views
from .views import RecursoCreate, ArchivoCreate, RecursoListView, EditarPlanProduccion, crearPlanProduccion, RecursoDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('planProduccion/<int:idRecurso>', views.viewPlanProduccion, name='view-plan'),
    path('crear-plan-produccion/<int:idRecurso>', views.crearPlanProduccion, name='crear-plan'),
    path('editar-plan-produccion/<int:idRecurso>', views.EditarPlanProduccion, name='editar-plan'),
    path('crear-entrada/<int:idRecurso>', views.createEntradaPlan, name='create-entrada'),
    path('crear-recurso/', RecursoCreate.as_view(), name='create-recurso'),
    path('crear-archivo/<int:id_recurso>', ArchivoCreate.as_view(), name='create-archivo'),
    path('recursos/', RecursoListView.as_view(), name='recursos'),
    path('recurso/<int:pk>', RecursoDetailView.as_view(), name='recurso'),
]
