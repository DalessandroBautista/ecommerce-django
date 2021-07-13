from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=40)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre




class Usuario(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    user = models.CharField(max_length=64, default='USER001')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'
def __str__(self):
        return f"Nombre: {self.name} email: {self.email}"


class Producto(models.Model):
    
    nombre = models.CharField(max_length=64)
    image = models.ImageField(upload_to='productos')
    description = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=0)
    precio = models.FloatField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    stock=models.BooleanField(default=True)
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    def __str__(self):
        return f"Producto: #{self.nombre} Descripcion: {self.description}, Precio: {self.precio}" 
        
class Compra(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    producto=models.ManyToManyField(Producto)
    created=models.DateTimeField(auto_now_add=True)