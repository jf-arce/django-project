from django import forms
from .models import Consulta

class AddPacienteForm(forms.Form): 
    name = forms.CharField(label="Nombre", max_length=50)
    surname = forms.CharField(label="Apellido", max_length=50)
    age = forms.IntegerField(label="Edad")

class CreateConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['date', 'description', 'price', 'paciente']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Esto hace que el campo se renderice como un campo de fecha en HTML
            'description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'Escribe una descripción aquí...',
                'class': 'form-control',  # Si usas Bootstrap, por ejemplo
                'maxlength': 1000,
                'style': 'resize: none;',  # Esto permitirá al usuario redimensionar el campo solo verticalmente
            }),
        }