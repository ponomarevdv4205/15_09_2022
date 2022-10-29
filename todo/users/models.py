from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(('Email address'), unique=True, )

    def __str__(self):
        return self.lastname


class Project(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(default='url')
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    text = models.TextField(blank=True, null=True)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
