from django.contrib import admin
from django.urls import path
from . import  views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home', views.home, name = 'home'),
    path('pizza', views.pizza, name = 'pizza'),
    path('pasta', views.pasta, name = 'pasta'),
    path('lasagna', views.lasagna, name = 'lasagna'),
    path('', views.signup, name = "signup"),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name='logout'),
    path('success', views.success, name ='success'),
    path('cart', views.cart, name = 'cart'),
    path('menu', views.menu, name = 'menu'),
    path('contact', views.contact, name = "contact"),
    path('feedback', views.feedback, name = "feedback"),
    path("feedback-success", views.feedsuccess, name = "feedsuccess"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
