from django.urls import path
from Autos.views import automoviles,motocicletas,create_product,buscar_producto_view,camionetas,detail_product_autos,delete_products

urlpatterns =[
    path("", automoviles, name = "automoviles"),
    path("motocicletas/", motocicletas, name = "motocicletas"),
    path("camionetas/", camionetas, name = "camionetas"),
    path("create_product/", create_product, name = "create_product"),
    path("buscar_producto/",buscar_producto_view, name="buscar_producto"),
    path("detail_product_autos/<int:pk>/",detail_product_autos, name="detail_product_autos"),
    path("delete_products/<int:pk>/",delete_products, name="delete_products"),
    ]
