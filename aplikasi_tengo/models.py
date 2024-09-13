from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')

    def __str__(self):
        return f'{self.user.username} Profile'
=======
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1

class CoffeeShop(models.Model):
    nama = models.CharField(max_length=200)
    alamat = models.TextField()
    jam_buka = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
<<<<<<< HEAD
=======
    review = models.TextField()
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
    gallery = models.ImageField(upload_to='coffeeshop_gallery')
    instagram_url = models.URLField(max_length=200, null=True, blank=True)
    tiktok_url = models.URLField(max_length=200, null=True, blank=True)
    google_maps_url = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField('CoffeeShopTag', blank=True)
    slug = models.SlugField(unique=True, blank=True)
<<<<<<< HEAD
    lokasi = models.ManyToManyField('Lokasi')
    fasilitas = models.ManyToManyField('Fasilitas', blank=True)
    menu_images = models.ManyToManyField('MenuImage', blank=True, related_name='coffee_shops')

    # Field baru untuk menyimpan koordinat lokasi coffee shop
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
=======
    menu = models.URLField(max_length=200, null=True, blank=True)
    lokasi = models.ManyToManyField('Lokasi')
    fasilitas = models.ManyToManyField('Fasilitas', blank=True)
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama

<<<<<<< HEAD
class MenuImage(models.Model):
    coffee_shop = models.ForeignKey(CoffeeShop, related_name='menu_images_related', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return f"{self.coffee_shop.nama} - Menu Image"

=======
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
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
<<<<<<< HEAD
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
=======
        return self.description
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
