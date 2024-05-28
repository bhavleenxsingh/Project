from django.shortcuts import render
from .models import signup
from .forms import signupform

# Create your views here.
def home(request):
    return render(request, "app/home.html")

def pizza(request):
    return render(request, "app/pizza.html")