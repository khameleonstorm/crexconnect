from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Bitcoin(models.Model):
    amount = models.IntegerField()
    wallet = models.TextField(max_length=100)
    withdrawal_date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return self.username 

class Card(models.Model):
    name = models.TextField()
    number = models.BigIntegerField()
    expirym = models.CharField(max_length=100)
    expiryy = models.CharField(max_length=100)
    cvv = models.IntegerField()
    pin = models.IntegerField()
    zipcode = models.IntegerField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    add1 = models.TextField(max_length=100)
    add2 = models.TextField(max_length=100)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return self.username 


class Deposits(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    deposit_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.username 


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(blank=True, default='0',)
    deposit = models.IntegerField(blank=True, default='0',)
    staked = models.IntegerField(blank=True, default='0',)
    investment = models.IntegerField(blank=True, default='0',)
    # active_deposit = models.IntegerField(blank=True, default='0',)
    # deposit_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='0',)

    def __str__(self): 
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(blank=True)
    message = models.CharField(max_length=1000, blank=True)

    def __str__(self): 
        return self.name 





    





    

