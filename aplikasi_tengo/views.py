<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from .models import CoffeeShop, GambarLowongan, Subscription, Lokasi, Recommendation, VisitStatus, UserProfile
=======
from django.shortcuts import render, get_object_or_404
from .models import CoffeeShop, GambarLowongan, Subscription, Lokasi, Recommendation
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
<<<<<<< HEAD
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth.models import User
=======
import random
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1

def index(request):
    return render(request, 'index.html')

<<<<<<< HEAD
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun berhasil dibuat untuk {username}! Silakan login untuk melanjutkan.')
            return redirect('login')  # Alihkan ke halaman login
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username atau password salah.')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Anda berhasil logout.')
    return redirect('login')

@login_required
def profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        messages.error(request, "Profil pengguna tidak ditemukan. Silakan hubungi admin.")
        return redirect('home')

    # Ambil coffee shop yang telah dikunjungi atau ingin dikunjungi
    visited_shops = CoffeeShop.objects.filter(visitstatus__user=request.user, visitstatus__status='visited')
    visit_later_shops = CoffeeShop.objects.filter(visitstatus__user=request.user, visitstatus__status='visit_later')

    return render(request, 'profile.html', {
        'profile': profile,
        'visited_shops': visited_shops,
        'visit_later_shops': visit_later_shops,
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil berhasil diperbarui!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
=======
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
def home(request):
    query = request.GET.get('q')
    lokasi_id = request.GET.get('lokasi')

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

<<<<<<< HEAD
@login_required
def filtered_location(request, location_id):
    selected_location = get_object_or_404(Lokasi, pk=location_id)
=======

def filtered_location(request, location_id):
    selected_location = Lokasi.objects.get(pk=location_id)
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
    coffee_shops = CoffeeShop.objects.filter(lokasi=selected_location)

    return render(request, 'home.html', {'coffee_shops': coffee_shops})

<<<<<<< HEAD
@login_required
=======
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
def detail_coffeeshop(request, slug):
    coffee_shop = get_object_or_404(CoffeeShop, slug=slug)
    context = {
        'coffee_shop': coffee_shop,
    }
    return render(request, 'detail_coffeeshop.html', context)

<<<<<<< HEAD
@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def disclaimer(request):
    return render(request, 'disclaimer.html')

@login_required
def not_found(request, exception):
    return render(request, '404.html')

@login_required
=======
def about(request):
    return render(request, 'about.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')

def not_found(request, exception):
    return render(request, '404.html')

>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
def gambar_lowongan(request):
    gambar_lowongan = GambarLowongan.objects.all()
    return render(request, 'gambar_lowongan.html', {'gambar_lowongan': gambar_lowongan})

<<<<<<< HEAD
@login_required
=======
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
def recommendation(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'recommendation.html', {'recommendations': recommendations})

<<<<<<< HEAD
@login_required
=======
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
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

<<<<<<< HEAD
@login_required
def success(request):
    return render(request, 'success.html')

@login_required
def map_view(request):
    coffee_shops = CoffeeShop.objects.all()
    context = {'coffee_shops': coffee_shops}
    return render(request, 'map.html', context)

@login_required
def save_visit_status(request, coffee_shop_id, status):
    coffee_shop = get_object_or_404(CoffeeShop, id=coffee_shop_id)
    visit_status, created = VisitStatus.objects.get_or_create(
        user=request.user,
        coffee_shop=coffee_shop,
        defaults={'status': status}
    )
    
    if not created:
        visit_status.status = status
        visit_status.save()

    messages.success(request, f'Status kunjungan untuk {coffee_shop.nama} berhasil diperbarui')
    return redirect('detail_coffeeshop', slug=coffee_shop.slug)
=======
def success(request):
    return render(request, 'success.html')
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
