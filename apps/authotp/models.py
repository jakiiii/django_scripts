import uuid
import datetime
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

from apps.authotp.manager import UserManager


class User(AbstractUser):
    username = None
    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        max_length=32
    )
    is_verified = models.BooleanField(
        default=False
    )
    otp = models.CharField(
        max_length=6,
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email


'''  ALL SIGNALS HERE  '''


@receiver(user_logged_in)
def _user_logged_in(sender, user, request, **kwargs):
    try:
        user.last_login_time = datetime.datetime.now()
        user.save()
    except Exception as e:
        print(e)


@receiver(user_logged_out)
def _user_logged_out(sender, user, request, **kwargs):
    try:
        user.last_logout_time = datetime.datetime.now()
        user.save()
    except Exception as e:
        print(e)
