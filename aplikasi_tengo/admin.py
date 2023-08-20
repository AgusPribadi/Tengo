from django.contrib import admin
from .models import CoffeeShop, CoffeeShopImage

class CoffeeShopImageInline(admin.TabularInline):
    model = CoffeeShopImage
    extra = 1  # Number of empty image forms to display

@admin.register(CoffeeShop)
class CoffeeShopAdmin(admin.ModelAdmin):
    inlines = [CoffeeShopImageInline]  # Add the inline for images