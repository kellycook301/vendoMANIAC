from django.shortcuts import render
from rest_framework import viewsets
from .models import Beverage, Coin
from .serializers import BeverageSerializer, CoinSerializer

class BeverageView(viewsets.ModelViewSet):
    queryset = Beverage.objects.all()
    serializer_class = BeverageSerializer

class CoinView(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
