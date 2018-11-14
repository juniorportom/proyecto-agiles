from django.urls import path
from SGRD import views
from .views import RecursoCreate, ArchivoCreate, RecursoListView,  RecursoDetailView, ClipCreate

urlpatterns = [
    path('', views.index, name='index'),
    path('ver-plan-produccion/<int:idRecurso>', views.verPlanProduccion, name='view-plan'),
    path('crear-plan-produccion/<int:idRecurso>', views.crearPlanProduccion, name='crear-plan'),
    path('editar-plan-produccion/<int:idRecurso>', views.EditarPlanProduccion, name='editar-plan'),
    path('exportar-plan-produccion/<int:idRecurso>', views.exportarPlanProduccion, name='exportar-plan'),
    path('crear-entrada/<int:idRecurso>', views.createEntradaPlan, name='create-entrada'),
    path('editar-entrada/<int:idEntrada>', views.editarEntradaPlan, name='editar-entrada'),
    path('crear-recurso/', RecursoCreate.as_view(), name='create-recurso'),
    path('crear-archivo/<int:id_recurso>', ArchivoCreate.as_view(), name='create-archivo'),
    path('recursos/', RecursoListView.as_view(), name='recursos'),
    path('recurso/<int:pk>', RecursoDetailView.as_view(), name='recurso'),
    path('buscar/', views.recursoBusqueda, name='busqueda'),
    path('crear-clip/<int:id_recurso>', ClipCreate.as_view(), name='crear-clip'),
    path('clips/<int:idArchivo>', views.archivoClips, name='ver-clips'),
    path('crear-recurso/crear-tipo', views.crear_tipo, name='crear-tipo'),
    path('tags', views.manage_tags, name='manage-tags'),
    path('tag/<int:id_tag>/delete', views.delete_tag, name='delete-tag'),
    path('recurso/<int:pk>/remove-tag/<int:id_tag>', views.remove_tag, name='remove-tag'),
    path('recurso/<int:pk>/add-tag', views.add_tag, name='add-tag'),
    path('clip/<int:pk>/remove-tag/<int:id_tag>/<int:id_archivo>', views.remove_tag_clip, name='remove-tag-clip'),
    path('clip/<int:pk>/add-tag/<int:id_archivo>', views.add_tag_clip, name='add-tag-clip')
]
