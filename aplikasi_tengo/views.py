from django.shortcuts import render, get_object_or_404
from .models import CoffeeShop, GambarLowongan
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Subscription
import random

def index(request):
    return render(request, 'index.html')

def home(request):
    query = request.GET.get('q')
    coffee_shops = CoffeeShop.objects.all()

    if query:
        coffee_shops = coffee_shops.filter(Q(nama__icontains=query) | Q(alamat__icontains=query))

    # Acak daftar Coffee Shop
    coffee_shops = list(coffee_shops)
    random.shuffle(coffee_shops)

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
                      'Ketika Tengo update, kami akan automatis mengirimkan ke email kamu 😊'
            from_email = ''
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return HttpResponseRedirect(reverse('success'))
    
    return render(request, 'footer.html')

def success(request):
    return render(request, 'success.html')