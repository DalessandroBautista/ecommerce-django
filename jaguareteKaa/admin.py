from django.contrib import admin
from .models import Producto, Usuario, Categoria, Compra
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
class UserAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
class CompraAdmin(admin.ModelAdmin):
    readonly_field=('created')
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario, UserAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Categoria, CategoriaAdmin)