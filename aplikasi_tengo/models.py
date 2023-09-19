from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class CoffeeShopTag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class CoffeeShop(models.Model):
    nama = models.CharField(max_length=200)
    alamat = models.TextField()
    jam_buka = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    review = models.TextField()
    gallery = models.ImageField(upload_to='coffeeshop_gallery')
    instagram_url = models.URLField(max_length=200, null=True, blank=True)
    tiktok_url = models.URLField(max_length=200, null=True, blank=True)
    google_maps_url = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField('CoffeeShopTag', blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama
    
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
    email = models.EmailField(unique=True)  # Simpan alamat email pengguna yang berlangganan
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Waktu langganan dibuat
    is_active = models.BooleanField(default=True)  # Status langganan (aktif/nonaktif)

    def __str__(self):
        return self.email