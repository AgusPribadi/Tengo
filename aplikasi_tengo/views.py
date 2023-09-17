from django.shortcuts import render, get_object_or_404
from .models import CoffeeShop, GambarLowongan
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def home(request):
    # Ambil atau buat sesi untuk menyimpan jumlah tampilan
    if 'total_page_views' not in request.session:
        request.session['total_page_views'] = 1
    else:
        request.session['total_page_views'] += 1

    # Dapatkan hasil pencarian jika ada
    query = request.GET.get('q')
    if query:
        coffee_shops = CoffeeShop.objects.filter(Q(nama__icontains=query) | Q(alamat__icontains=query))
    else:
        coffee_shops = CoffeeShop.objects.all()

    return render(request, 'home.html', {'coffee_shops': coffee_shops, 'total_page_views': request.session['total_page_views']})

def detail_coffeeshop(request, slug):
    coffee_shop = get_object_or_404(CoffeeShop, slug=slug)
    context = {
        'coffee_shop': coffee_shop,
    }
    return render(request, 'detail_coffeeshop.html', context)

def about(request):
    return render(request, 'about.html')

def not_found(request, exception):
    return render(request, '404.html')

def gambar_lowongan(request):
    gambar_lowongan = GambarLowongan.objects.all()
    return render(request, 'gambar_lowongan.html', {'gambar_lowongan': gambar_lowongan})