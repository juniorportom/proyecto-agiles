from django.urls import path

from SGRD.views.recurso import RecursoCreate, RecursoListView,  RecursoDetailView, recursoBusqueda
from SGRD.views.index import index
from SGRD.views.archivo import ArchivoCreate
from SGRD.views.clip import archivoClips, ClipCreate, ClipDelete
from SGRD.views.planProduccion import crearPlanProduccion, EditarPlanProduccion, delete_plan, createEntradaPlan, editarEntradaPlan, verPlanProduccion, exportarPlanProduccion, delete_entrada
from SGRD.views.descargarArchivo import planear_descarga, editar_plan_descarga, check_for_downloads
from SGRD.views.etiqueta import manage_tags, delete_tag, remove_tag, add_tag, remove_tag_clip, add_tag_clip
from SGRD.views.tipo import crear_tipo


urlpatterns = [
    path('', index, name='index'),
    path('ver-plan-produccion/<int:idRecurso>', verPlanProduccion, name='view-plan'),
    path('crear-plan-produccion/<int:idRecurso>', crearPlanProduccion, name='crear-plan'),
    path('editar-plan-produccion/<int:idRecurso>', EditarPlanProduccion, name='editar-plan'),
    path('eliminar-plan-produccion/<int:idPlan>', delete_plan, name='eliminar-plan'),
    path('eliminar-entrada/<int:idEntrada>', delete_entrada, name='eliminar-entrada'),
    path('exportar-plan-produccion/<int:idRecurso>', exportarPlanProduccion, name='exportar-plan'),
    path('crear-entrada/<int:idRecurso>', createEntradaPlan, name='create-entrada'),
    path('editar-entrada/<int:idEntrada>', editarEntradaPlan, name='editar-entrada'),
    path('crear-recurso/', RecursoCreate.as_view(), name='create-recurso'),
    path('crear-archivo/<int:id_recurso>/<int:terminado>', ArchivoCreate.as_view(), name='create-archivo'),
    path('recursos/', RecursoListView.as_view(), name='recursos'),
    path('recurso/<int:pk>', RecursoDetailView.as_view(), name='recurso'),
    path('buscar/', recursoBusqueda, name='busqueda'),
    path('crear-clip/<int:id_recurso>', ClipCreate.as_view(), name='crear-clip'),
    path('clips/<int:idArchivo>', archivoClips, name='ver-clips'),
    path('crear-recurso/crear-tipo', crear_tipo, name='crear-tipo'),
    path('tags', manage_tags, name='manage-tags'),
    path('tag/<int:id_tag>/delete', delete_tag, name='delete-tag'),
    path('recurso/<int:pk>/remove-tag/<int:id_tag>', remove_tag, name='remove-tag'),
    path('recurso/<int:pk>/add-tag', add_tag, name='add-tag'),
    path('clip/<int:pk>/remove-tag/<int:id_tag>/<int:id_archivo>', remove_tag_clip, name='remove-tag-clip'),
    path('clip/<int:pk>/add-tag/<int:id_archivo>', add_tag_clip, name='add-tag-clip'),
    path('clips/<int:idArchivo>/remove-clip/<int:pk>', ClipDelete.as_view(), name='eliminar-clip'),
    path('recurso/<int:id_recurso>/archivo/<int:id_archivo>', planear_descarga, name='descargar-archivo'),
    path('recurso/<int:id_recurso>/archivo/<int:id_archivo>/editar', editar_plan_descarga, name='editar-descargar-archivo'),
    path('descargas-programadas', check_for_downloads, name='check-descargas'),
]
