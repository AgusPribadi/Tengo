from django.shortcuts import render, get_object_or_404, redirect
from .models import CoffeeShop, GambarLowongan, Subscription, Lokasi, Recommendation, VisitStatus, UserProfile
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Simpan pengguna baru
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            
            # Membuat profil secara otomatis untuk pengguna baru
            UserProfile.objects.create(user=user)
            
            messages.success(request, f'Akun berhasil dibuat untuk {username} dengan email {email}! Silakan login untuk melanjutkan.')
            return redirect('login')  # Alihkan ke halaman login
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Mengambil email dari form
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)  # Autentikasi dengan username dari email
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Kamu berhasil masuk!')
            return redirect('home')
        else:
            messages.error(request, 'Email atau password salah.')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Anda berhasil logout.')
    return redirect('login')

@login_required
def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        messages.error(request, "Profil pengguna tidak ditemukan. Silakan hubungi admin.")
        return redirect('home')

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


def home(request):
    query = request.GET.get('q')
    lokasi_id = request.GET.get('lokasi')

    # Mengambil semua coffee shop dan mengurutkan dari yang terbaru
    coffee_shops = CoffeeShop.objects.all().order_by('-created_at')

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
    selected_location = get_object_or_404(Lokasi, pk=location_id)
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


def disclaimer(request):
    return render(request, 'disclaimer.html')


def not_found(request, exception):
    return render(request, '404.html')


def gambar_lowongan(request):
    gambar_lowongan = GambarLowongan.objects.all()
    return render(request, 'gambar_lowongan.html', {'gambar_lowongan': gambar_lowongan})


def recommendation(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'recommendation.html', {'recommendations': recommendations})


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

class RobotsView(View):
    def get(self, request, *args, **kwargs):
        sitemap_url = f"{request.scheme}://{request.get_host()}/sitemap.xml"
        content = f"""
        User-agent: *
        Disallow:

        Sitemap: {sitemap_url}
        """
        return HttpResponse(content, content_type="text/plain")