from django.db import models

class VendingMachine(models.Model):
    name = models.CharField(max_length=50)
    total_coins = models.IntegerField()
    purchase_price = models.IntegerField()
    

class Beverage(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Coin(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name