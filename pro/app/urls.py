from django.contrib import admin
from django.urls import path
from . import  views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name = 'home'),
    path('pizza', views.pizza, name = 'pizza'),
    path('pasta', views.pasta, name = 'pasta'),
    path('lasagna', views.lasagna, name = 'lasagna'),
    path('signup', views.signup, name = "signup"),
    path('login', views.login, name = 'login'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
