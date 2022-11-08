from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class User(AbstractUser):
class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=128, null=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    is_staff = models.BooleanField(
        _("staff status"),
        default=False)

    def __str__(self):
        return self.username


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    url = models.URLField(default='url')
    users = models.ManyToManyField(User, related_name="projects")

    def __str__(self):
        return self.name


class ToDo(models.Model):
    text = models.TextField(blank=True, null=True)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
