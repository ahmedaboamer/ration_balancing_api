from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#for create our UserProfileManager
from django.contrib.auth.models import BaseUserManager

#create our manger for userprofile class
class UserProfileManager(BaseUserManager):
    """class for our custom UserProfileManager."""
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('users must have an email!')
        email = self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,name,password=None):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """a custom user model in the application that inherits from django user model """
    email = models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active =models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

#To add functionality to our customized user class and it is required by django
    object = UserProfileManager()
#some django user model fields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['name']
#some django functions
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
