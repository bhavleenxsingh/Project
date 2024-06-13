from django import forms
from .models import signupmodel
from .models import feedmodel
from .models import loginmodel
    
class signupform(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    Confirm_Password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = signupmodel
        fields = ['Username', 'Password', 'Confirm_Password']


class feedform(forms.ModelForm):
    class Meta:
        model = feedmodel 
        fields = ['Name','Mobile','Email','Message']
        
class loginform(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    class Meta:
        model = loginmodel
        fields = ['Username', 'Password']
        
widgets = {
            'Password': forms.PasswordInput(),
            'Confirm_Password': forms.PasswordInput(), 
        }