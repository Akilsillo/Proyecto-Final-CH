from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        hepl_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Ingrese su email")
    password1 = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
    