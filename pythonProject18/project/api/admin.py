from django.contrib import admin
from .models import Products, Cart, Order, User

admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(User)


