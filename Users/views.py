from django.shortcuts import render
from Users.forms import UserRegisterForm
# Login/Logout/CreateUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Principal/index.html")
        
    else:
        form = UserRegisterForm()
        
    return render(request, "Users/register.html", {"form":form})

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            
            users = authenticate(username=user, password=pwd)
            
            if users is not None:
                login(request, users)
                return render(request, "Principal/index.html", {"mensaje":f"Has iniciado sesion con exito {user}"})
            else:
                form = AuthenticationForm()
                return render(request, "Users/login.html", {"mensaje":f"Error, datos incorrectos", "form":form})
            
        else:
            form = AuthenticationForm()
            return render(request, "Users/login.html", {"mensaje":f"Error, formulario inválido"})
    
    form = AuthenticationForm()
    return render(request, "Users/login.html", {"form":form})