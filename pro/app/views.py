from django.shortcuts import render
from django.http import HttpResponse
from .models import signupf
from .forms import signupform
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, "app/home.html")

def pizza(request):
    return render(request, "app/pizza.html")

def signup(request):
    if request.method == 'POST':
        synup = signupform(request.POST, request.FILES)
        print(synup)
        if synup.is_valid():
            print(synup)
            synup.save()
            return redirect(home)
        else :
            return HttpResponse("Error in submitting form.")
    else:
        synup = signupform()
        return render(request, "app/signup.html", {'synup':synup})



    # return render(request, "app/signup.html")