from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)


class Hobbie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.ManyToManyField(Profile, blank=True)
