from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from .models import signupf

from .forms import signupform
from . forms import feedform

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

def success(request):
    return render(request, "app/success.html")

def cart(request):
    return render(request, "app/cart.html")

def menu(request):
    return render(request, "app/menu.html")

def contact(request):
    return render(request, "app/contact.html")

def feedsuccess(request):
    return render(request, "app/feedsuccess.html")   

def feedback(request):
    if request.method == 'POST':
        feed = feedform(request.POST, request.FILES)
        print(feed)
        if feed.is_valid():
            print(feed)
            feed.save()
            return redirect(feedsuccess)
    else :
        feed = feedform()
        return render(request, "app/feedback.html", {'feed': feed})

def signup(request):
    if request.method == 'POST':
        synup = signupform(request.POST, request.FILES)
        print(synup)
        if synup.is_valid():
            print("Form is valid.")
            password = request.POST.get('Password')
            confirm_password = request.POST.get('Confirm_Password')
            if password == confirm_password:
                print("Passwords match.")
                print(synup)
                synup.save()
                return redirect(success)
            else :
                return HttpResponse("Passwords do not match.")
        else :
            return HttpResponse("Form Invalid.")
    else:
        synup = signupform()
        return render(request, "app/signup.html", {'synup':synup})
    
