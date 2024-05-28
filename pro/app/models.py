from django.db import models

# Create your models here.
class signup(models.Model):
    Username = models.CharField(max_length = 15, null = False, blank = False)
    Password = models.CharField(max_length = 10, null = False, blank = False)