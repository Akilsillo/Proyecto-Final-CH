from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Ingrese su email")
    password1 = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput, required=False)
    
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    
    imagen = forms.ImageField(required=False)

    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
    