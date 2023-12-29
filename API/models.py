from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    identity = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='media', null=True, blank=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media', null=True, blank=True)

    def photo_url(self):
        if self.photo:
            return self.photo.url
        return None

class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField()
    position = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media', null=True, blank=True)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='menus', null=True, blank=True)

    def photo_url(self):
        if self.photo:
            return self.photo.url
        return None

class Food(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to='media', null=True, blank=True)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    total = models.FloatField()
    status = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.IntegerField()

# Facturacion
class BillHeader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class BillDetail(models.Model):
    BillHeader = models.ForeignKey(BillHeader, on_delete=models.CASCADE, default=1)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()