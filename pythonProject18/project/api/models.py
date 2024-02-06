from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    fio = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , 'fio']


class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Order(models.Model):
    products = models.ManyToManyField(Products)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.emaul