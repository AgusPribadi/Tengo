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
from .forms import CustomUserCreationForm, UserProfileForm, ContactForm
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.contrib.sitemaps import Sitemap

# Untuk Views Halaman Index
def index(request):
    return render(request, 'index.html')

# Untuk Views Halaman Register
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

# Untuk Views Halaman Login
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

# Untuk Views Logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Anda berhasil logout.')
    return redirect('login')

# Untuk Views Halaman Profile
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

# Untuk Views Halaman Edit Profile
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

# Untuk Views Halaman Home
def home(request):
    query = request.GET.get('q')
    lokasi_id = request.GET.get('lokasi')

    coffee_shops = CoffeeShop.objects.all().order_by('-created_at')

    if query:
        coffee_shops = coffee_shops.filter(Q(nama__icontains=query) | Q(alamat__icontains=query))

    if lokasi_id:
        coffee_shops = coffee_shops.filter(lokasi__id=lokasi_id)

    locations = Lokasi.objects.all()

    total_coffee_shops = coffee_shops.count()

    return render(request, 'home.html', {'coffee_shops': coffee_shops, 'total_coffee_shops': total_coffee_shops, 'locations': locations})

# Untuk Views Fitur Filter
def filtered_location(request, location_id):
    selected_location = get_object_or_404(Lokasi, pk=location_id)
    coffee_shops = CoffeeShop.objects.filter(lokasi=selected_location)

    return render(request, 'home.html', {'coffee_shops': coffee_shops})

# Untuk Views Detail CoffeeShop
def detail_coffeeshop(request, slug):
    coffee_shop = get_object_or_404(CoffeeShop, slug=slug)
    context = {
        'coffee_shop': coffee_shop,
    }
    return render(request, 'detail_coffeeshop.html', context)

# Untuk Views Halaman About
def about(request):
    return render(request, 'about.html')

# Untuk Views Halaman Disclaimer 
def disclaimer(request):
    return render(request, 'disclaimer.html')

# Untuk Views Halaman Not Found 404
def not_found_404(request, exception):
    return render(request, '404.html', status=404)

# Untuk Views Halaman Not Found 500
def not_found_500(request):
    return render(request, '500.html', status=500)

# Untuk Views Halaman Loker
def gambar_lowongan(request):
    gambar_lowongan = GambarLowongan.objects.all()
    return render(request, 'gambar_lowongan.html', {'gambar_lowongan': gambar_lowongan})

# Untuk Views Halaman Recommendation
def recommendation(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'recommendation.html', {'recommendations': recommendations})

# Untuk Views Subscribe
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

# Untuk Views Halaman Sukses
def success(request):
    return render(request, 'success.html')

# Untuk Views Halaman Maps
def map_view(request):
    coffee_shops = CoffeeShop.objects.all()
    context = {'coffee_shops': coffee_shops}
    return render(request, 'map.html', context)

# Untuk Views Fitur Kunjungan
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

# Untuk Robots Crawler
class RobotsView(View):
    def get(self, request, *args, **kwargs):
        sitemap_url = f"{request.scheme}://{request.get_host()}/sitemap.xml"
        
        # Konten untuk robots.txt
        content = (
            "User-agent: *\n"
            "Disallow: /admin/\n\n"
            f"Sitemap: {sitemap_url}\n"
        )
        
        return HttpResponse(content, content_type="text/plain")

# Untuk Views Contact
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Membuat pesan untuk dikirim
        subject = f'Pesan dari {name}'
        full_message = f'Dari: {name}\nEmail: {email}\nPesan:\n{message}'

        # Mengirim email
        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['hitengo2023@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'success.html')
    
    return render(request, 'index.html')

# Halaman Privacy Policy
def privacy_policy(request):
    return render(request, 'privacy_policy.html')

# Halaman Contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
            email = form.cleaned_data['email']
            pesan = form.cleaned_data['pesan']

            send_mail(
                f'Pesan dari {nama}',
                pesan,
                email,
                ['hitengo2023@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# Halaman Sitemap
def sitemap_view(request):
    # Ambil semua coffee shop untuk ditampilkan dalam sitemap
    coffee_shops = CoffeeShop.objects.all().order_by('-created_at')
    
    # URL untuk halaman statis
    static_pages = [
        {'name': 'Home', 'url': reverse('index')},
        {'name': 'Tentang Kami', 'url': reverse('about')},
        {'name': 'Kontak', 'url': reverse('contact')},
        {'name': 'Privacy Policy', 'url': reverse('privacy_policy')},
        {'name': 'Disclaimer', 'url': reverse('disclaimer')},
    ]
    
    context = {
        'coffee_shops': coffee_shops,
        'static_pages': static_pages,
    }
    return render(request, 'sitemap.html', context)