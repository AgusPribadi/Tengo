from django.shortcuts import render, get_object_or_404
from .models import CoffeeShop, GambarLowongan
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Subscription, Lokasi
import random

def index(request):
    return render(request, 'index.html')

def home(request):
    query = request.GET.get('q')
    lokasi_id = request.GET.get('lokasi')  # Mendapatkan ID lokasi yang dipilih

    coffee_shops = CoffeeShop.objects.all()

    if query:
        coffee_shops = coffee_shops.filter(Q(nama__icontains=query) | Q(alamat__icontains=query))

    # Jika ada filter berdasarkan lokasi yang dipilih, filter berdasarkan lokasi tersebut
    if lokasi_id:
        coffee_shops = coffee_shops.filter(lokasi__id=lokasi_id)

    # Ambil semua lokasi untuk dropdown select
    locations = Lokasi.objects.all()

    total_coffee_shops = coffee_shops.count()  # Menghitung jumlah total Coffee Shop

    return render(request, 'home.html', {'coffee_shops': coffee_shops, 'total_coffee_shops': total_coffee_shops, 'locations': locations})


def filtered_location(request, location_id):
    selected_location = Lokasi.objects.get(pk=location_id)
    coffee_shops = CoffeeShop.objects.filter(lokasi=selected_location)

    return render(request, 'home.html', {'coffee_shops': coffee_shops})

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

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Save the subscription to the database
        subscription, created = Subscription.objects.get_or_create(email=email)

        # If the subscription was newly created (not a duplicate email)
        if created:
            # Send a confirmation email
            subject = 'Berlangganan Tengo Berhasil'
            message = 'Selamat! Email kamu telah berlangganan di Tengo. ' \
                      'Ketika Tengo update, kami akan otomatis mengirimkan ke email kamu 😊'
            from_email = 'hitengo2023@gmail.com'
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return HttpResponseRedirect(reverse('success'))
    
    return render(request, 'footer.html')

def success(request):
    return render(request, 'success.html')