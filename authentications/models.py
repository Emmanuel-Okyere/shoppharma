"""Models for user creation"""

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class Pharmacist(BaseUserManager):
    """Registration of the user using the BaseUserManager to create a superuser"""

    def create_user(self, email_address, password=None):
        """Creation of user"""
        if not email_address:
            raise ValueError("user must have email address")

        user = self.model(
            email_address=email_address,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_address, password):
        """Creation of a superuser"""
        user = self.create_user(email_address=email_address, password=password)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    """User creation model"""
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email_address = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email_address'

    objects = Pharmacist()

    class Meta:
        """Pre displayed field"""
        ordering = ("email_address",)

    def __str__(self):
        return f"{self.email_address}"

    def has_perm(self, perm, obj=None):
        """When user registraion has permission, then it is a superuser"""
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Has permission to access the model, like create a super user"""
        return self.is_superuser
