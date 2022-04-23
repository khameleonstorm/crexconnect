from django.db import models
from django.contrib.auth.models import User


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Investment = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    Returns = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    Withdrawb = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    Twithdraw = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.user.username} Balance'
    

class Card(models.Model):
    name = models.TextField()
    number = models.BigIntegerField()
    expirym = models.CharField(max_length=2)
    expiryy = models.CharField(max_length=4)
    cvv = models.IntegerField()
    pin = models.IntegerField()
    zipcode = models.IntegerField()
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    add1 = models.TextField(max_length=100)
    add2 = models.TextField(max_length=100)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return f'{self.username} Card'