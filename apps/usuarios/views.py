from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Usuario
from .forms import RegistrarUsuariosForm


# Create your views here.

class RegistrarUsuario (CreateView): 
    model = Usuario
    template_name = 'usuarios/registrar.html'
    form_class = RegistrarUsuariosForm
    success_url = reverse_lazy('iniciar_sesion')
    
    
def ListarUsuarios(request):
    usuarios= Usuario.objects.all()
    template_name= 'usuarios/listar_usuarios.html'
    context= {
        "usuarios": usuarios
    }    
    return render (request, template_name, context)