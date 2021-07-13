from django.urls import path, re_path
from . import views
from .views import Inicio

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', Inicio.as_view(), name="index"),
    path('about', views.about, name="about"),
    path('carrito', views.carrito, name="carrito"),
    path('producto/<int:producto_id>/', views.ver_producto, name="producto"),
    path('editProducto/<int:producto_id>/', views.editar_producto, name="editProducto"),
    path('busqueda/', views.buscar, name="buscar"),
    path('contacto', views.contacto, name="contacto"),
    path('nuevoProducto', views.nuevoProducto, name="nuevoProducto"),
    path('eliminarP/<int:producto_id>/', views.eliminar_producto_db, name="eliminar_producto"),
    path('categoria/<nombre>/', views.categoria, name="categoria"),
    path('login', LoginView.as_view(template_name="poloticHtml/registration/login.html"), name="login"),
    path('register', views.registrarse, name="register"),
    path('logout', LogoutView.as_view(template_name="poloticHtml/registration/logged_out.html"), name="logout"),
    path('password_reset', views.password_reset, name="password_reset"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('comprar/<int:producto_id>/', views.comprar_producto, name="comprar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),

]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)