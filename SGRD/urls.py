from django.urls import path
from SGRD import views

urlpatterns = [
    path('', views.index, name='index'),
]
