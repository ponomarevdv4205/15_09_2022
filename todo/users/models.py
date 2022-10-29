from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    Email = models.EmailField(('Email address'), unique=True, )

    def __str__(self):
        return self.lastname


class ToDo(models.Model):
    text = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)
