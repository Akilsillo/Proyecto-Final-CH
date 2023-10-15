from django.shortcuts import render
from Users.models import Avatar

# Create your views here.

def home(request):

    return render(request, "Principal/index.html")