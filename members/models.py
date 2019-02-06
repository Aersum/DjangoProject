from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save


class Hobby(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, null=True, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/profile_img', blank=True)
    hobby = models.ManyToManyField(Hobby, blank=True, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)


class Event(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None, null=True
        )
    image = models.ImageField(upload_to='images/event_img', blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    hobby = models.ForeignKey(
        Hobby,
        on_delete=models.CASCADE,
        default=None,
        null=True
        )

    def __str__(self):
        return self.title
