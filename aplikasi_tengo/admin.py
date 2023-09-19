from django.contrib import admin
from .models import CoffeeShop, CoffeeShopTag, CoffeeShopImage, GambarLowongan, Subscription
from django.http import HttpResponse
import csv

class CoffeeShopImageInline(admin.TabularInline):
    model = CoffeeShopImage
    extra = 1

class CoffeeShopAdmin(admin.ModelAdmin):
    inlines = [CoffeeShopImageInline]
    actions = ['download_data_as_csv']

    def download_data_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="coffee_shops.csv"'

        writer = csv.writer(response)
        writer.writerow(['Nomor', 'Nama', 'Alamat', 'Jam Buka', 'Kontak', 'Review', 'Instagram URL', 'TikTok URL', 'Google Maps URL'])

        for index, coffee_shop in enumerate(queryset, start=1):
            writer.writerow([index, coffee_shop.nama, coffee_shop.alamat, coffee_shop.jam_buka, coffee_shop.contact, coffee_shop.review, coffee_shop.instagram_url, coffee_shop.tiktok_url, coffee_shop.google_maps_url])

        return response

    download_data_as_csv.short_description = 'Download Data as CSV'

admin.site.register(CoffeeShop, CoffeeShopAdmin)
admin.site.register(GambarLowongan)
admin.site.register(CoffeeShopTag)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']

admin.site.register(Subscription, SubscriptionAdmin)