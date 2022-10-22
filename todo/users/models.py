from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(('email address'), unique=True,)
