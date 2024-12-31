from django.db import models
from datetime import date
# Create your models here.

class Paciente(models.Model): 
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name + " " + self.surname
    
class Medicamento(models.Model): 
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
class MedicamentoXPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)

class Consulta(models.Model):
    date = models.DateField(default= date.today)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=4000.00)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.date.strftime("%d/%m/%Y") + " - " + self.paciente.name + " " + self.paciente.surname + " - " + self.description
