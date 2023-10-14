from django.urls import path
from Users.views import *
from django.contrib.auth.views import LogoutView
# Function views
urlpatterns = [
    path('register/', register, name='Register'),
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='Principal/index.html'), name="Logout"),
    path('edit/', edit, name="Edit"),
]

# Class views
urlpatterns += [
    
]