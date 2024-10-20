
from django.contrib import admin
from django.urls import path, include
from .views import inicio


from .views import *
from apps.usuarios.views import RegistrarUsuario
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name= 'apps.usuarios'

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name='inicio'),
    path("usuarios/", include('apps.usuarios.urls')),
    path("registrar/", RegistrarUsuario.as_view(), name= 'registrar'),
    path('acerca_de/', acerca_de, name='acerca_de' ),
    path('contacto/', contacto, name='contacto'),
    path("publicaciones/", include('apps.publicaciones.urls')),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
