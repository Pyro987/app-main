# mi_aplicacion/forms.py

from django import forms
from .models import Publicaciones, Comentarios

class PublicacionesForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['titulo', 'empresa', 'descripcion', 'categoria', 'published', 'imagen']
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model= Comentarios 
        fields = ['mensaje']

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar'}))

