from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.conf import settings #imagen
from django.conf.urls.static import static #imagen
from Consesionario.views import saludo,index,login_view,logout_view,register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/",saludo),
    path("",index, name = "index"),
    path("login/",login_view, name = "login_view"),
    path("logout/",logout_view, name = "logout_view"),
    path("register/",register_view, name = "register_view"),
    path("automoviles/",include("Autos.urls"))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
