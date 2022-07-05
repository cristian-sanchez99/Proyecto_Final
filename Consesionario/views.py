from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from Autos.models import Autos
from Consesionario.forms import User_registration_form 



def saludo(request):
    return HttpResponse("Saludo de prueba")

def index(request):
    autos = Autos.objects.all()
    context = {"autos":autos}
    return render(request,"index.html",context=context)



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                context = {"message":f"Bienvenido {username}!!"}
                return render(request,"index.html",context=context)
            else:
                form = AuthenticationForm()
                context = {"error":"Usuario no encontrado"}
                return render(request,"auth/login.html",context = context)
        else:
            error = form.errors
            form = AuthenticationForm()
            context = {"error":error,"form":form}
            return render(request,"auth/login.html",context = context)
    else:
        form = AuthenticationForm()
        context = {"form":form}
        return render(request,"auth/login.html",context = context)

def logout_view(request):
    logout(request)
    return redirect("index")

def register_view(request):
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username = username, password = password)
            login(request,user)
            context = {"message":f"Usuario creado correctamente. Bienvenido {username}"}
            return render(request,"index.html",context = context)
        else: 
            errors = form.errors
            form = User_registration_form()
            context = {"errors":errors, "form":form}
            return render(request, "auth/register.html",context = context)
    else:
        form = User_registration_form()
        context = {"form":form}
        return render(request,"auth/register.html",context=context)