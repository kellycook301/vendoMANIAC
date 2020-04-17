from rest_framework import serializers
from .models import Beverage, Coin

# class VendingMachineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vending_Machine
#         fields = ('id', 'name', 'total_coins', 'purchase_price', )

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = ('id', 'name', 'price', 'quantity')

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id', 'name', 'value', 'quantity')