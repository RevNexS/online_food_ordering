from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest

# Create your models here.
# class Customers(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128, verbose_name='password', help_text='USE A STRONG PASSWORD')
#     phone = models.CharField(max_length=20)

#     def __str__(self):
#         return "".format(self.first_name, self.last_name)


class Address(models.Model):
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    customer_id = models.ForeignKey("CustomerUser",on_delete=models.CASCADE , blank=True , null=True)

    def __str__(self):
        return f"{self.street_address}, {self.city},{self.pincode}"


class CustomerUserManager(BaseUserManager):
    
    def create_user(self,email , password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user        


class CustomerUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    # password = models.CharField(max_length=128, verbose_name='password', help_text='USE A STRONG PASSWORD')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ,
        related_name="customuser_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )

    objects = CustomerUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

# FIXME [] Email is not unique. two user can have same email.    

class CustomerUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomerUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomerUser.DoesNotExist:
            return None

# TODO [] Create a table for Customer Order (What they have order, Their address, food Quantity).
# TODO [] Create a table for Payment (What method of payment was used, How much was paid, Was any coupon applied.)