from django.contrib import admin
from .models import Beverage, Coin, VendingMachine

admin.site.register(Beverage)
admin.site.register(Coin)
admin.site.register(VendingMachine)

# Register your models here.
