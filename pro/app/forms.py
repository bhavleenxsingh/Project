from django import forms
from .models import signupf
from .models import feedmodel
    
class signupform(forms.ModelForm):
    class Meta:
        model = signupf
        fields = '__all__'

    def clean_password(self):
        Password = self.get("Password")
        Confirm_Password = self.get("ConfirmPassword")
        if Password and Confirm_Password and Password != Confirm_Password:
            raise forms.ValidationError("Passwords don't match")
        return Confirm_Password

class feedform(forms.ModelForm):
    class Meta:
        model = feedmodel 
        fields = '__all__'