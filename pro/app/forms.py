from django import forms
from .models import signup

class signupform(forms.ModelForm):
    model = signup
    fields = '__all__'
    