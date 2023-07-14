from django import forms
from planificacion.models import Meta

class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = '__all__'  # Incluye todos los campos del modelo Meta en el formulario
