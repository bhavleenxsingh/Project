from django.db import models


# Create your models here.
class signupf(models.Model):
    Username = models.CharField(max_length = 25, null = False, unique = True, primary_key=True, default = " ")
    Password = models.CharField(max_length = 20, null = True, blank = True)
    Confirm_Password = models.CharField(max_length = 20, null = True, blank = True)
    
    def __str__(self):
        return f'{self.Username} ,{self.Password}, {self.Confirm_Password}'    

class feedmodel(models.Model):
    Name = models.CharField(max_length=20, blank = False)
    Mobile = models.CharField(max_length=10 ,blank = False)
    Email = models.EmailField(null = True, blank = True)
    Message = models.TextField(max_length = 300, null = False, blank = False, default = " ")
    
    def __str__(self):
        return f'{self.Name}, {self.Mobile}, {self.Email}, {self.Message}'