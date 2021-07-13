from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto
class FormularioContacto(forms.Form):
    asunto=forms.CharField(label="Asunto",required=True)
    email=forms.EmailField(label="Emai",required=True)
    mensaje=forms.CharField(label="Contenido", widget=forms.Textarea)
    


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class': 'usuario'}), max_length=150, required=True, )
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(), max_length=30, required=True, )
class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class': 'usuario'}), max_length=150, required=True, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Al menos 8 caracteres y no pueden ser todos numeros.')
    password2 = forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Ingrese la misma contraseña que antes, para verificación.')
    first_name = forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'nombre'}), max_length=30, required=False, help_text='Opcional.')
    last_name = forms.CharField(
        label='Apellido', widget=forms.TextInput(attrs={'class': 'apellido'}), max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'email'}), max_length=254, required=True, help_text='Se requiere una direccion de email valida.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ProductoForm(forms.ModelForm):

    
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'categoria', 'image', 'description')
        labels= {
            'nombre': 'Titulo ',
            'image': 'Imagen ',
            'description': 'Descripcion ',
            'categoria': 'Categoria ',
            'precio': 'Precio ',
        }
        widgets= {
            'description': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder':'Ingrese una descripción'}),
            'nombre': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder':'Ingrese un titulo de producto'})
        }
class UpdateProductoForm(forms.ModelForm):   
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'categoria', 'image', 'description')
        labels= {
            'nombre': 'Titulo ',
            'image': 'Imagen ',
            'description': 'Descripcion ',
            'categoria': 'Categoria ',
            'precio': 'Precio ',
        }
        widgets= {
            'description': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder':'Ingrese una descripción'}),
            'nombre': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder':'Ingrese un titulo de producto'})
        }
    def save(self):
        prod= self.instance
        prod.nombre= self.cleaned_data['nombre']
        prod.description= self.cleaned_data['description']
        prod.categoria= self.cleaned_data['categoria']
        prod.precio= self.cleaned_data['precio']

        if self.cleaned_data['image']:
            prod.image= self.cleaned_data['image']
        prod.save()
        return prod