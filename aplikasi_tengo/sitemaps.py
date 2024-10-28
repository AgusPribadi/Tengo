from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import CoffeeShop

class CoffeeShopSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # Mengembalikan daftar CoffeeShop yang diurutkan berdasarkan tanggal pembuatan
        return CoffeeShop.objects.all().order_by('-created_at')

    def location(self, obj):
        # Menggunakan metode `get_absolute_url` dari model
        return obj.get_absolute_url()


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        # Nama URL untuk halaman statis yang ingin dimasukkan dalam sitemap
        return ['index', 'about', 'contact', 'privacy_policy', 'disclaimer']

    def location(self, item):
        # Mendapatkan lokasi berdasarkan nama URL
        return reverse(item)
