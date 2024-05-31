from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from .models import signupf

from .forms import signupform


# Create your views here.
def home(request):
    return render(request, "app/home.html")

def pizza(request):
    return render(request, "app/pizza.html")


def pasta(request):
    return render(request, "app/pasta.html")


def lasagna(request):
    return render(request, "app/lasagna.html")


def login(request):
    return render(request, "app/login.html")

def signup(request):
    if request.method == 'POST':
        synup = signupform(request.POST, request.FILES)
        print(synup)
        if synup.is_valid():
            print(synup)
            synup.save()
            return redirect(signup)
        else :
            return HttpResponse("Error in submitting form.")
    else:
        synup = signupform()
        return render(request, "app/signup.html", {'synup':synup})
    
