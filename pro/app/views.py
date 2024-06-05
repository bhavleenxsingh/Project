from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  signupmodel
from .forms import  feedform, loginform, signupform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, "app/home.html")

@login_required(login_url='login')
def pizza(request):
    return render(request, "app/pizza.html")

@login_required(login_url='login')
def pasta(request):
    return render(request, "app/pasta.html")

@login_required(login_url='login')
def lasagna(request):
    return render(request, "app/lasagna.html")

# def login(request):
#     if request.method == "POST":
#         loginuser = loginform(request.POST)
#         if loginuser.is_valid():
#             username = loginuser.get('Username')
#             password = loginuser.get('Password')
            
#             try:
#                 user = signupmodel.objects.get(Username=username)
    
#                 if user.Password == password:
#                     return redirect('menu')  # Ensure 'menu' is the correct URL name or view name
#                 else:
#                     return HttpResponse("Wrong Password")
#             except signupmodel.DoesNotExist:
#                 return HttpResponse("User does not exist")
#         else:
#             return HttpResponse("Invalid form data")
#     else:
#         loginuser = loginform()
#         return render(request, "app/login.html", {"loginuser": loginuser})

def success(request):
    return render(request, "app/success.html")

@login_required(login_url='login')
def cart(request):
    return render(request, "app/cart.html")

@login_required(login_url='login')
def menu(request):
    return render(request, "app/menu.html")

def contact(request):
    return render(request, "app/contact.html")

def feedsuccess(request):
    return render(request, "app/feedsuccess.html")

def feedback(request):
    if request.method == 'POST':
        feed = feedform(request.POST, request.FILES)
        if feed.is_valid():
            feed.save()
            return redirect('feedsuccess')
    else:
        feed = feedform()
    return render(request, "app/feedback.html", {'feed': feed})


def signup(request):
    if request.method == 'POST':
        synup1 = signupform(request.POST)
        if synup1.is_valid():
            username = synup1.cleaned_data.get('Username')
            password = synup1.cleaned_data.get('Password')
            confirm_password = synup1.cleaned_data.get('Confirm_Password')
            if password == confirm_password:
                User.objects.create_user(username=username, password=password)
                synup1.save()
                return redirect('success')
            else:
                return HttpResponse("Passwords do not match.")
        else:
            return HttpResponse("Form Invalid.")
    else:
        synup1 = signupform()
    return render(request, "app/signup.html", {'synup1': synup1})

def logout(request):
    auth_logout(request)
    return redirect('login')

def login(request):
    if request.method == "POST":
        loginuser = loginform(request.POST)
        if loginuser.is_valid():
                username = loginuser.cleaned_data.get('Username')
                password = loginuser.cleaned_data.get('Password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect(menu)
                else :
                    return HttpResponse("Wrong Username or Password")
        else :
            return HttpResponse("Form invalid.")
    else :
        loginuser = loginform()
        return render(request, "app/login.html", {"loginuser": loginuser})        

# def login(request):
#     if request.method == "POST":
#         loginuser = loginform(request.POST)
#         if loginuser.is_valid():
#             username = loginuser.get('Username')
#             password = loginuser.get('Password')
            
#             try:
#                 user = signupmodel.objects.get(Username=username)
    
#                 if user.Password == password:
#                     return redirect('menu')  # Ensure 'menu' is the correct URL name or view name
#                 else:
#                     return HttpResponse("Wrong Password")
#             except signupmodel.DoesNotExist:
#                 return HttpResponse("User does not exist")
#         else:
#             return HttpResponse("Invalid form data")
#     else:
#         loginuser = loginform()
#         return render(request, "app/login.html", {"loginuser": loginuser})


# def login(request): ###---------------------------------------------------------------------------------------- WORKING
#     if request.method == "POST":
#         loginuser = loginform(request.POST)
#         if loginuser.is_valid():
#             username = loginuser.cleaned_data.get('Username')
#             password = loginuser.cleaned_data.get('Password')
            
#             try:
#                 user = signupmodel.objects.get(Username=username)
#                 if user.Password == password:
#                     return redirect('menu')  # Ensure 'menu' is the correct URL name or view name
#                 else:
#                     return HttpResponse("Wrong Password")
#             except signupmodel.DoesNotExist:
#                 return HttpResponse("User does not exist")
#         else:
#             return HttpResponse("Invalid form data")
#     else:
#         loginuser = loginform()
#         return render(request, "app/login.html", {"loginuser": loginuser})