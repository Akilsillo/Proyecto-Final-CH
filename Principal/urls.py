from django.urls import path
from Principal.views import *

urlpatterns = [
    path('home/', home, name="Home"),
    path('about/', about, name="About"),
]