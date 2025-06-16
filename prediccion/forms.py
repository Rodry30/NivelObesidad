from django import forms
from . import models

class PrediccionForm(forms.ModelForm):
    class Meta:
        model = models.FormPrediccion
        fields = [
            'genero', 'edad', 'estatura', 'peso', 'afdeo', 'favc', 'fcvc', 'ncp',
            'caec', 'tabaco', 'ch20', 'scc', 'faf', 'tue', 'calc', 'mtrans'
        ]
        labels = {
            'genero': 'Género',
            'edad': 'Edad',
            'estatura': 'Estatura (m)',
            'peso': 'Peso (kg)',
            'afdeo': 'Antecedentes familiares con sobrepeso',
            'favc': '¿Consume comida alta en calorías con frecuencia?',
            'fcvc': 'Frecuencia de consumo de vegetales',
            'ncp': 'Número de comidas principales',
            'caec': 'Comida entre comidas',
            'tabaco': '¿Fuma tabaco?',
            'ch20': 'Consumo de agua',
            'scc': 'Monitoreo de calorías',
            'faf': 'Frecuencia de actividad física',
            'tue': 'Tiempo de uso de dispositivos electrónicos',
            'calc': 'Consumo de alcohol',
            'mtrans': 'Medio de transporte habitual',
        }
        widgets = {
            'genero': forms.RadioSelect(),
            'afdeo': forms.RadioSelect(),
            'favc': forms.RadioSelect(),
            'fcvc': forms.RadioSelect(),
            'ncp': forms.RadioSelect(),
            'caec': forms.RadioSelect(),
            'tabaco': forms.RadioSelect(),
            'ch20': forms.RadioSelect(),
            'scc': forms.RadioSelect(),
            'faf': forms.RadioSelect(),
            'tue': forms.RadioSelect(),
            'calc': forms.RadioSelect(),
            'mtrans': forms.RadioSelect(),

            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'estatura': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'peso': forms.NumberInput(attrs={
                'type': 'range',
                'class': 'form-range',
                'min': '30',
                'max': '300',
                'step': '1',
                'oninput': 'document.getElementById("pesoOutput").value = this.value'
            }),
        }

