from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(models.Model):
    avatar = models.ImageField(upload_to="image/usuarios/")
    
    
class Usuario (AbstractUser):
    nombre = models.CharField(max_length=20, null=True)
    apellido= models.CharField(max_length=20, null=True)
    edad= models.CharField(max_length=2, null=True)
    is_staff= models.BooleanField( 'es_staff', default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios',default='usuarios/inicio_sesion.png')
    #profile= models.ForeignKey(Profile)
    
    def __str__(self):
        return self.nombre 
    