from rest_framework import serializers
from .models import Beverage, Coin

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = ('id', 'name', 'price', 'quantity')

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id', 'name', 'value', 'quantity')