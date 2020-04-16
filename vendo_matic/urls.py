from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('inventory', views.BeverageView)
router.register('coin', views.CoinView)

urlpatterns = [
    path('', include(router.urls))
]