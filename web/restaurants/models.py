from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest

class RestroUserManager(BaseUserManager):
    
    def create_user(self,email , password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user        


class RestroUser(AbstractBaseUser, PermissionsMixin):
    # password = models.CharField(max_length=128, verbose_name='password', help_text='USE A STRONG PASSWORD')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250)
    # phone = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=250, null=True)
    street = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=6 , null=True)
    images_path = models.ImageField(upload_to='images/' , null=True)
    menu_id = models.ForeignKey('RestroMenu', on_delete=models.CASCADE , null=True)
    timing = models.CharField(max_length=100 , null=True)
    stars = models.IntegerField(null=True , blank=True)
    desc = models.TextField(null=True , blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ,
        related_name="restro_user_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="restro_user_set",
        related_query_name="user",
    )

    objects = RestroUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class RestroUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = RestroUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except RestroUser.DoesNotExist:
            return None


class RestroMenu(models.Model):
    restro = models.ForeignKey(RestroUser, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    menu_images = None

class RestroMenuImage(models.Model):
    restro_menu_id = models.ForeignKey(RestroMenu , related_name="images" , on_delete=models.CASCADE )
    image = models.ImageField(upload_to="img/restro_img")

class RestroMenuImage(models.Model):
    restro_user_id = models.ForeignKey(RestroUser , related_name="images" , on_delete=models.CASCADE )
    image = models.ImageField(upload_to="img/menu_img")
