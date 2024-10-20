
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import *
from . import views

app_name = 'apps.publicaciones'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(), name='agregar_categoria'),
    path("agregar_publicaciones/", views.agregar_publicaciones, name='agregar_publicaciones'),
    path("ver_publicaciones/", VerPublicaciones.as_view(), name='ver_publicaciones'),
    path("detalle/<int:pk>/", DetallePublicacion.as_view(), name='detalle'),
    path("agregar_comentario/<int:pk>/", agregar_comentario, name='agregar_comentario'),
    path('buscar/', views.buscar_publicaciones, name='buscar_publicaciones'),
    path("editar_publicacion/<int:pk>/", agregar_publicaciones, name='editar_publicacion'),
    path("eliminar_publicacion/<int:pk>/", EliminarPublicacion.as_view(), name='eliminar_publicacion'),
    path('comentario/editar/<int:pk>/', views.editar_comentario, name='editar_comentario'),
    path('comentario/eliminar/<int:pk>/', views.eliminar_comentario, name='eliminar_comentario'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
