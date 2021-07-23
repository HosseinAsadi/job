from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('User must provide username')

        user = self.model(username=username)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        """create and save a new superuser with given details"""
        user = self.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)

    f_name = models.CharField(max_length=50, null=True, blank=True)

    l_name = models.CharField(max_length=50, null=True, blank=True)

    mobile = models.CharField(max_length=11, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)

    gender = models.IntegerField(default=0)

    cv = models.FileField(null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
