from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')

    def __str__(self):
        return f'{self.user.username} Profile'


class CoffeeShop(models.Model):
    nama = models.CharField(max_length=200)
    alamat = models.TextField()
    jam_buka = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    gallery = models.ImageField(upload_to='coffeeshop_gallery', null=True)
    instagram_url = models.URLField(max_length=200, null=True, blank=True)
    tiktok_url = models.URLField(max_length=200, null=True, blank=True)
    google_maps_url = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField('CoffeeShopTag', blank=True)
    slug = models.SlugField(unique=True, blank=True)
    lokasi = models.ManyToManyField('Lokasi')
    fasilitas = models.ManyToManyField('Fasilitas', blank=True)
    menu_link = models.URLField('MenuLink', blank=True)
    tahun_berdiri = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    CASH = 'Cash'
    QRIS = 'QRIS'

    PAYMENT_CHOICES = [
        (CASH, 'Cash'),
        (QRIS, 'QRIS'),
    ]

    metode_pembayaran = models.ManyToManyField('PaymentMethod', blank=True)

    def get_absolute_url(self):
        return reverse('detail_coffeeshop', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

class MenuImage(models.Model):
    coffee_shop = models.ForeignKey(CoffeeShop, related_name='menu_images_related', on_delete=models.CASCADE)
    image_url = models.URLField(default='')  # Default nilai kosong

    def __str__(self):
        return f"{self.coffee_shop.nama} - Menu Image"


class Fasilitas(models.Model):
    MUSHOLLA = 'Musholla'
    AC = 'AC'
    VIP_ROOM = 'VIP Room'
    PERMAINAN = 'Permainan'

    FASILITAS_CHOICES = [
        (MUSHOLLA, 'Musholla'),
        (AC, 'AC'),
        (VIP_ROOM, 'VIP Room'),
        (PERMAINAN, 'Permainan'),
    ]

    nama_fasilitas = models.CharField(max_length=20, choices=FASILITAS_CHOICES, unique=True)

    def __str__(self):
        return self.nama_fasilitas


class CoffeeShopTag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Lokasi(models.Model):
    nama_lokasi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_lokasi


class CoffeeShopImage(models.Model):
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='coffeeshop_images')

    def __str__(self):
        return f"Image for {self.coffee_shop.nama}"


class GambarLowongan(models.Model):
    gambar = models.ImageField(upload_to='lowongan_gambar')

    def __str__(self):
        return f"Image for {self.gambar}"


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Recommendation(models.Model):
    tweet_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.description


class VisitStatus(models.Model):
    VISIT_CHOICES = [
        ('visit_later', 'Ingin Dikunjungi'),
        ('visited', 'Sudah Dikunjungi'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=VISIT_CHOICES, default='visit_later')

    class Meta:
        unique_together = ('user', 'coffee_shop')

    def __str__(self):
        return f"{self.user.username} - {self.coffee_shop.nama} - {self.get_status_display()}"


class PaymentMethod(models.Model):
    nama_metode = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nama_metode
