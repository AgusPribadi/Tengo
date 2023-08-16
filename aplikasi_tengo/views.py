from django.shortcuts import render, get_object_or_404
from .models import CoffeeShop
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def home(request):
    query = request.GET.get('q')
    if query:
        coffee_shops = CoffeeShop.objects.filter(Q(nama__icontains=query) | Q(alamat__icontains=query))
    else:
        coffee_shops = CoffeeShop.objects.all()
    
    return render(request, 'home.html', {'coffee_shops': coffee_shops})

def detail_coffeeshop(request, coffee_shop_id):
    coffee_shop = get_object_or_404(CoffeeShop, id=coffee_shop_id)
    context = {
        'coffee_shop': coffee_shop,
    }
    return render(request, 'detail_coffeeshop.html', context)

def about(request):
    return render(request, 'about.html')

def not_found(request, exception):
    return render(request, '404.html')