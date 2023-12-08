from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    Username = models.CharField(max_length=50)
    Firstname = models.CharField(max_length=50,null=True)
    Lastname = models.CharField(max_length=50,null=True)
    NationalCode = models.CharField(max_length=10,null=True)
    Gender = models.BooleanField(default=True)
    Mobile = models.CharField(max_length=11,null=True)
    Address = models.CharField(max_length=200)
    ExpireDate = models.DateTimeField(null=True)
    email = models.CharField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email