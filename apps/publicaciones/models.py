from django.db import models
from django.utils import timezone
from apps.usuarios.models import Usuario
from django import forms 

# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=20, null= False)
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class Publicaciones(models.Model):
    titulo = models.CharField(max_length=30, null=False)
    empresa = models.CharField(max_length=20, null=False)
    descripcion = models.TextField()
    fecha_agregado= models.DateTimeField(auto_now_add=True)
    is_staff= models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    published= models.DateTimeField(blank=False, default=timezone.now)
    imagen= models.ImageField(null=True, blank=True, upload_to='publicaciones', default='publicaciones/trabajos_default.jpg')
    categoria= models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.titulo}"
    
    class Meta:
        ordering = ('-published',)
    
class Comentarios(models.Model):
    publicacion= models.ForeignKey(Publicaciones, on_delete=models.CASCADE, related_name='comentarios')
    autor= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje= models.TextField()
    
    def __str__(self):
        return f"{self.autor.username}"