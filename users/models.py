from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

def default_user_settings():
    return {
        "theme": {
            "main": "defaultDark",
            "footer": "defaultDark",
            "navbar": "defaultDark",
            "toolbar": "defaultDark"
        },
        "layout": {
            "style": "layout1",
            "config": {
                "mode": "fullwidth",
                "footer": {
                    "style": "fixed",
                    "display": False,
                    "position": "below"
                },
                "navbar": {
                    "folded": True,
                    "display": True,
                    "position": "left"
                },
                "scroll": "content",
                "toolbar": {
                    "style": "fixed",
                    "display": True,
                    "position": "below"
                },
                "leftSidePanel": {
                    "display": False
                },
                "rightSidePanel": {
                    "display": True
                }
            }
        },
        "direction": "ltr",
        "animations": True,
        "notifications": {
            "muted": True,
            "disabled": True
        },
        "customScrollbars": True
    }


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, **other_fields):
        if not email:
            raise ValueError('You must provide an email')

        if not password:
            raise ValueError('You must provide a password')

        if not first_name:
            raise ValueError('You must provide a first name')

        if not last_name:
            raise ValueError('You must provide a last name')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **other_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        return self.create_user(email=email, password=password, first_name=first_name, last_name=last_name,
                                is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=16, null=True, blank=True)
    last_name = models.CharField(max_length=16, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_logged_in = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    settings = models.JSONField(default=default_user_settings, null=False, blank=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
