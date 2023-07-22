# aplikasi_tengo/models.py

from django.db import models

class CoffeeShop(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)
    jam_buka = models.CharField(max_length=100)
    gallery = models.ImageField(upload_to='coffee_shop_gallery/')
    contact = models.CharField(max_length=20)
    review = models.TextField()

    def __str__(self):
        return self.nama
