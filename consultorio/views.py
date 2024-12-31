from django.http import HttpResponse
from .models import Paciente, Consulta
from django.shortcuts import get_object_or_404, render, redirect
from .forms import AddPacienteForm, CreateConsultaForm
# Create your views here.

def index(request): 
    title = "Bienvenido al consultorio"
    return render(request, 'index.html', {
        "title": title
    })

def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/pacientes.html", {
        "pacientes": pacientes
    })

#Implementar
def paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    return render(request, "pacientes/paciente.html", {
        "paciente": paciente
    })

def consultas(request):
    consultas = Consulta.objects.all()
    return render(request, "consultas/consultas.html", {
        "consultas": consultas
    })

def add_paciente(request): 
    if request.method == 'GET':
        return render(request, 'pacientes/agregar-paciente.html', {
            'form': AddPacienteForm()
        })
    else:
        Paciente.objects.create(name=request.POST['name'],
        surname=request.POST['surname'], age=request.POST['age'])
        return redirect('pacientes')

def create_consulta(request): 
    if request.method == 'GET':
        return render(request, 'consultas/crear-consulta.html', {
            'form': CreateConsultaForm()
        })
    else:
        Consulta.objects.create(date=request.POST['date'], 
        description=request.POST['description'], price=request.POST['price'],
        paciente_id= request.POST['paciente'])
        return redirect('consultas')