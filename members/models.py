from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Hobby(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/profile_img', blank=True)
    hobby = models.ManyToManyField(Hobby, blank=True)


class Event(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None, null=True
        )
    image = models.ImageField(upload_to='images/event_img', blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, default=None, null=True)
