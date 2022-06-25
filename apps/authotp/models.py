import uuid
import datetime
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.signals import user_logged_in, user_logged_out

from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# from apps.authotp.manager import UserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Phone number is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_('Phone number is required'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone_number = models.CharField(
        max_length=18,
        unique=True
    )
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


# ALL SIGNALS HERE
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
