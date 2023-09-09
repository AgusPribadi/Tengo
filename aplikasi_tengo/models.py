from django.db import models

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