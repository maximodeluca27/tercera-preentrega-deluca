from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm,CustomUserCreationForm
from django.http import HttpRequest,HttpResponse


def index(request):
    return render(request,"core/index.html")

def contacto(request):
    return render(request,"core/contacto.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name="core/login.html"

def register(request:HttpRequest)->HttpResponse:
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request,"core/index.html",{"mensaje":f"Usuario '{username}' creado "})
    else:
        form=CustomUserCreationForm()
    return render(request,"core/register.html",{"form":form})
