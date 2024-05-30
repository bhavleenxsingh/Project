from django import forms
from .models import signupf

class signupform(forms.ModelForm):
    model = signupf
    fields = '__all__'
    