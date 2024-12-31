from django.contrib import admin
from .models import Paciente, Consulta, Medicamento, MedicamentoXPaciente
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(Medicamento)
admin.site.register(MedicamentoXPaciente)