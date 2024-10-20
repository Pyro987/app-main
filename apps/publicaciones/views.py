from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, BaseDeleteView, DeleteView
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


class AgregarCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'publicaciones/agregar_categoria.html'
    success_url = reverse_lazy('apps.publicaciones:ver_publicaciones')
    

@login_required
def agregar_publicaciones(request, pk=None):
    instancia_existente = None
    if pk is not None:
        instancia_existente = get_object_or_404(Publicaciones, pk=pk)
    
    if request.method == 'POST':
        form = PublicacionesForm(request.POST, request.FILES, instance=instancia_existente)
        if form.is_valid():
            form.save()
            return redirect('apps.publicaciones:ver_publicaciones')
    else:
        form = PublicacionesForm(instance=instancia_existente)
        
    return render(request, 'publicaciones/agregar_publicaciones.html', {'form': form, 'instancia_existente': instancia_existente})



class VerPublicaciones(ListView):
    model= Publicaciones
    template_name= 'publicaciones/ver_publicaciones.html'
    context_object_name= 'publicaciones'
    ordering= ['-id']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categoria.objects.all()  
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_ids = self.request.GET.getlist('categoria')
        if categoria_ids:
            queryset = queryset.filter(categoria__id__in=categoria_ids)
        return queryset
    
    
class DetallePublicacion(DetailView):
    model= Publicaciones
    template_name= 'publicaciones/detalle_publicacion.html'
    context_object_name= 'publicacion'
    
    def get_context_data(self,**kwargs):
        publicacion= self.get_object()
        comentarios= publicacion.comentarios.all()
        context=super().get_context_data(**kwargs)
        context['comentarios']=comentarios
        context['comentario_form']=ComentarioForm()
        return context
    
@login_required
def agregar_comentario(request, pk):
    publicacion = get_object_or_404(Publicaciones, pk=pk)
    if request.method == "POST": 
        form = ComentarioForm(request.POST)
        if form.is_valid():
            
            comentario = form.save(commit=False)
            comentario.autor = request.user 
            comentario.publicacion = publicacion  # establecemos el campo para las publicaciones
            comentario.save()
            return redirect(reverse('apps.publicaciones:detalle', kwargs={'pk': pk}))
    else:
        form = ComentarioForm()

    return render(request, 'publicaciones/comentario/agregar_comentario.html', {'publicacion': publicacion, "formulario_comentario": form})

@login_required
def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentarios, pk=pk)

    if comentario.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este comentario.")

    publicacion = comentario.publicacion

    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect(reverse('apps.publicaciones:detalle', kwargs={'pk': publicacion.pk}))
    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'publicaciones/comentario/editar_comentario.html', {'comentario': comentario, 'publicacion': publicacion, 'formulario_comentario': form})


@login_required
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentarios, pk=pk)

    if request.method == "POST":
        comentario.delete()
        return redirect(reverse('apps.publicaciones:detalle', kwargs={'pk': comentario.publicacion.pk}))

    return render(request, 'publicaciones/comentario/eliminar_comentario.html', {'comentario': comentario})

class EditarPublicacion(LoginRequiredMixin, UpdateView):
    model = Publicaciones
    fields = ['titulo', 'empresa', 'descripcion', 'categoria', 'published', 'imagen']
    template_name = 'publicaciones/agregar_publicaciones.html'
    success_url = reverse_lazy('apps.publicaciones:ver_publicaciones')

    
class EliminarPublicacion(LoginRequiredMixin, DeleteView):
    model = Publicaciones
    template_name = 'publicaciones/confirma_eliminar.html'
    success_url = reverse_lazy('apps.publicaciones:ver_publicaciones')

def buscar_publicaciones(request):
    resultados = []
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Publicaciones.objects.filter(descripcion__icontains=termino_busqueda)
    else:
        form = BusquedaForm()

    return render(request, 'publicaciones/buscar_publicaciones.html', {'form': form, 'resultados': resultados})
