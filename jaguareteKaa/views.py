from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Usuario, Categoria, Compra
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from .carro import Carro
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView
from django.contrib import messages
# Create your views here.
categorias= Categoria.objects.all()
productos = Producto.objects.all()

productoWithImage= []
productoWithoutImage= []
for i in range(8):
        if (i <= 2):
            productoWithImage.append(productos[i])
        else:
            productoWithoutImage.append(productos[i])

class Inicio(TemplateView):
    template_name="poloticHtml/index.html"
    lista_productosImagen = Producto.objects.all().order_by("-id")[:3]
    lista_productosSinImagen = Producto.objects.all().order_by("-id")[3:9]

    def get(self,request, *args, **kwargs):
        return render (request, self.template_name, {"lista_productosImagen": self.lista_productosImagen,"lista_productosSinImagen": self.lista_productosSinImagen})
def index(request):
    
    return render(request, "poloticHtml/index.html",{
        "lista_productosImagen": productoWithImage,
        "lista_productosSinImagen": productoWithoutImage,
    })
def about(request):
    return render(request, "poloticHtml/about.html",{
        
    })
 

def ver_producto(request, producto_id):

    producto_ver=Producto.objects.get(id=producto_id)
    return render(request, "poloticHtml/producto.html",{
        "producto":  producto_ver,
       
    })
def editar_producto(request, producto_id):

    producto_ver=Producto.objects.get(id=producto_id)
    if request.method=="POST":
        producto_form =UpdateProductoForm(request.POST, request.FILES, instance = producto_ver)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('index')
    else:
        producto_form=UpdateProductoForm(instance = producto_ver)     
    return render(request, "poloticHtml/editar_producto.html",{
        "producto":  producto_ver,
        "producto_form": producto_form,
       
    })
def nuevoProducto(request):

    if request.method=="POST":
       producto_form=ProductoForm(request.POST, request.FILES)
       if producto_form.is_valid():
           producto_form.save()
           messages.success(request, 'Producto agregado')
           return redirect('index')
    else:
        producto_form=ProductoForm()     
    return render(request, "poloticHtml/nuevo_producto.html",{
        "producto_form": producto_form,
       
    })

def eliminar_producto_db(request, producto_id):
    producto=Producto.objects.get(id=producto_id)
    producto.delete()
    messages.success(request, "Producto eliminado")
    return redirect('index')


def categoria(request, nombre):
    categoria=Categoria.objects.get(nombre=nombre)
    productos=Producto.objects.filter(categoria=categoria)
    return render(request, "poloticHtml/categorias.html",{
        'categoria':categoria,
        'productos':productos
})

def contacto(request):
    if request.method=="POST":
       form=FormularioContacto(request.POST)
       if form.is_valid():
           infoForm=form.cleaned_data
           send_mail(infoForm['asunto'],infoForm['mensaje'], infoForm.get('email',''),['bautalobo@gmail.com'],)
           messages.success(request, 'Tu mensaje ha sido enviado!')
           return redirect('index')
    else:
        form=FormularioContacto()
    return render(request, "poloticHtml/formulario_contacto.html",{
        "form": form,
    })
def buscar(request):
    articulos=""
    mensaje="default"
    if request.GET["prd"]:

        producto=request.GET.get("prd")
        if len(producto)>20:
            messages.error(request, "Busqueda demasiado extensa")

        articulos=Producto.objects.filter(nombre__icontains=producto)
    else:
        mensaje= " No ha ingresado una busqueda"
    return render(request, "poloticHtml/search.html",{
        "productos": articulos,
        "mensaje":mensaje,       
    })

### Usuario
@login_required
def carrito(request):
    return render(request, "poloticHtml/carrito.html",{
    })

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()          
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'poloticHtml/registration/registro.html', {
        'form': form
        })
def login(request):
    if request.method=="POST":
       form=LoginForm(request.POST)
       if form.is_valid():
           return render(request, "poloticHtml/index.html")
    else:
        form=LoginForm()
    return render(request, "poloticHtml/registration/login.html",{
        "form": form,
    })
def register(request):
    return render(request, "poloticHtml/registration/register.html",{
       
    })
@login_required
def logout(request):
    return render(request, "poloticHtml/registration/logged_out.html",{
    })
def password_reset(request):
    return render(request, "poloticHtml/registration/password_reset_confirm.html",{
    })

### Carro
def comprar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    idp=producto.id
    carro.agregar(producto)
    messages.success(request, "Producto agregado al carrito")
    return redirect("index")

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    idp=producto.id
    carro.agregar(producto)
    return redirect("/carrito")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect("/carrito")
def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto)
    return redirect("/carrito")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("/carrito")