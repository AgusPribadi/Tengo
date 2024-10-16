from django.contrib.sitemaps import Sitemap
from .models import CoffeeShop

class CoffeeshopSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return CoffeeShop.objects.all()

    def get_absolute_url(self, obj):
        return obj.get_absolute_url()