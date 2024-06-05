from django.contrib import admin

# Register your models here
from .models import signupmodel, loginmodel, feedmodel
admin.site.register(signupmodel)
admin.site.register(loginmodel)
admin.site.register(feedmodel)