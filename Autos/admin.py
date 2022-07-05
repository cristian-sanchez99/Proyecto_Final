from django.contrib import admin
from Autos.models import Autos,Motocicletas,Camionetas
# Register your models here.
@admin.register(Autos)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name","price","SKU","active"] 


@admin.register(Camionetas)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name","price","SKU","active"]


@admin.register(Motocicletas)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name","price","SKU","active"]