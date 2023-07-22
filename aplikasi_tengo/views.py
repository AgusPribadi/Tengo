from django.shortcuts import render
from .models import CoffeeShop

def index(request):
    return render(request, 'index.html')

def home(request):
    coffee_shops = CoffeeShop.objects.all()
    return render(request, 'home.html', {'coffee_shops': coffee_shops})