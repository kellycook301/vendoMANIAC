from django.shortcuts import render
from rest_framework import viewsets
from .models import Beverage, Coin, VendingMachine
from .serializers import BeverageSerializer, CoinSerializer, VendingMachineSerializer

def index(request):
    print(request.headers['Host'])
    return render(request, 'templates/index.html', {'headers': request.headers})

class VendingMachineView(viewsets.ModelViewSet):
    queryset = VendingMachine.objects.all()
    serializer_class = VendingMachineSerializer

class BeverageView(viewsets.ModelViewSet):
    queryset = Beverage.objects.all()
    serializer_class = BeverageSerializer

# def out_of_stock(request):


class CoinView(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer

class HomeView(viewsets.ModelViewSet):
    template_name = 'templates/vending_machine.html'

# def inventory_detail_view(request):
#     if request.method == 'GET':
#         allBeverages = Beverage.objects.all()
#         context = {
#             'allBeverages': allBeverages
#         }
#     return render(request, "templates/index.html", context)