from django.db import models
from django.utils import timezone

# Create your models here.
class signupf(models.Model):
    Username = models.CharField(max_length = 25, null = False, unique = True, primary_key=True, default = " ")
    Password = models.CharField(max_length = 20, null = True, blank = True)
    Confirm_Password = models.CharField(max_length = 20, null = True, blank = True)
    # Date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.Username} ,{self.Password}, {self.Confirm_Password}'    
