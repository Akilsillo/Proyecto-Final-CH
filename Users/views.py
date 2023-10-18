from django.shortcuts import render
from Users.forms import UserRegisterForm, UserEditForm
from Users.models import Avatar
# Login/Logout/CreateUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
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

@login_required
def edit(request):
    
    usuario = request.user
    
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            if info["password1"] != info["password2"]:
                data = {
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                form = UserEditForm(initial=data)
            
            else:
                usuario.email= info['email']
                if info["password1"]:
                    usuario.set_password(info['password1'])
                usuario.first_name = info['first_name']
                usuario.last_name = info['last_name']
                usuario.save()
                
                try:
                    avatar = Avatar.objects.get(user=usuario)
                except Avatar.DoesNotExist:
                    avatar = Avatar(user=usuario, imagen=info["imagen"])
                    avatar.save()
                else:
                    avatar.imagen = info["imagen"]
                    avatar.save()
                    
                return render(request, "Principal/index.html")
        
    else:
        data = {
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        form = UserEditForm(initial=data)
    return render(request, "Users/edit.html", {"form": form, "user": usuario})
    
    