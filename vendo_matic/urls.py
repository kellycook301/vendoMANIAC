from django.urls import path, include
from . import views
from .views import BeverageView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('inventory', views.BeverageView)
router.register('coin', views.CoinView)
router.register('vending_machine', views.VendingMachineView)

# from vendo_matic.views import inventory_detail_view 

urlpatterns = [
    path('', include(router.urls)),
    path('inventory/', BeverageView, name="beverages-all")
]