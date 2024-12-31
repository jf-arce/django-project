from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pacientes/', views.pacientes, name="pacientes"),
    path('pacientes/<int:id>/', views.paciente, name="paciente"),
    path('pacientes/agregar-paciente/', views.add_paciente, name="agregar-paciente"),
    path('consultas/', views.consultas, name="consultas"),
    path('consultas/crear-consulta/', views.create_consulta, name="crear-consulta")
]