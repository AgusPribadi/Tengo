from django.contrib import admin
from .models import CoffeeShop, CoffeeShopImage

class CoffeeShopImageInline(admin.TabularInline):
    model = CoffeeShopImage
    extra = 1

@admin.register(CoffeeShop)
class CoffeeShopAdmin(admin.ModelAdmin):
    inlines = [CoffeeShopImageInline]