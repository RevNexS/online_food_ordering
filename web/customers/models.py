from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, verbose_name='password', help_text='USE A STRONG PASSWORD')
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "".format(self.first_name, self.last_name)


class Address(models.Model):
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street_address}, {self.city},{self.postal_code}"

