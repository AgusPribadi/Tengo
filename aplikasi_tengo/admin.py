from django.contrib import admin
<<<<<<< HEAD
from .models import (
    CoffeeShop, CoffeeShopTag, CoffeeShopImage, GambarLowongan, 
    Subscription, Lokasi, Fasilitas, Recommendation, VisitStatus,
    MenuImage
)
from django.http import HttpResponse
import csv
=======
from .models import CoffeeShop, CoffeeShopTag, CoffeeShopImage, GambarLowongan, Subscription, Lokasi, Fasilitas, Recommendation
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1

class CoffeeShopImageInline(admin.TabularInline):
    model = CoffeeShopImage
    extra = 1

<<<<<<< HEAD
class MenuImageInline(admin.TabularInline):
    model = MenuImage
    extra = 1

class CoffeeShopAdmin(admin.ModelAdmin):
    inlines = [CoffeeShopImageInline, MenuImageInline]
    actions = ['download_data_as_csv']

    list_display = ['nama', 'alamat', 'latitude', 'longitude', 'contact', 'instagram_url', 'google_maps_url']

    fields = [
        'nama', 'alamat', 'jam_buka', 'contact', 'gallery', 'instagram_url',
        'tiktok_url', 'google_maps_url', 'menu_images', 'latitude', 'longitude',
        'lokasi', 'fasilitas'
    ]

=======
class CoffeeShopAdmin(admin.ModelAdmin):
    inlines = [CoffeeShopImageInline]
    actions = ['download_data_as_csv']

>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
    def download_data_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="coffee_shops.csv"'

        writer = csv.writer(response)
<<<<<<< HEAD
        writer.writerow([
            'Nomor', 'Nama', 'Alamat', 'Jam Buka', 'Kontak', 
            'Instagram URL', 'TikTok URL', 'Google Maps URL', 
            'Menu', 'Latitude', 'Longitude'
        ])
=======
        writer.writerow(['Nomor', 'Nama', 'Alamat', 'Jam Buka', 'Kontak', 'Review', 'Instagram URL', 'TikTok URL', 'Google Maps URL', 'Menu', 'Lokasi'])
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1

        for index, coffee_shop in enumerate(queryset, start=1):
            writer.writerow([
                index, 
                coffee_shop.nama, 
                coffee_shop.alamat, 
                coffee_shop.jam_buka, 
<<<<<<< HEAD
                coffee_shop.contact,
                coffee_shop.instagram_url, 
                coffee_shop.tiktok_url, 
                coffee_shop.google_maps_url,
                coffee_shop.menu_images,
                coffee_shop.latitude,
                coffee_shop.longitude
=======
                coffee_shop.contact, 
                coffee_shop.review, 
                coffee_shop.instagram_url, 
                coffee_shop.tiktok_url, 
                coffee_shop.google_maps_url,
                coffee_shop.menu 
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
            ])

        return response

    download_data_as_csv.short_description = 'Download Data as CSV'

class FasilitasAdmin(admin.ModelAdmin):
    list_display = ['nama_fasilitas']

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']

<<<<<<< HEAD
class VisitStatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'coffee_shop', 'status']
    list_filter = ['status', 'user']

=======
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
admin.site.register(CoffeeShop, CoffeeShopAdmin)
admin.site.register(GambarLowongan)
admin.site.register(CoffeeShopTag)
admin.site.register(Lokasi)
admin.site.register(Recommendation)
admin.site.register(Fasilitas, FasilitasAdmin)
<<<<<<< HEAD
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(VisitStatus, VisitStatusAdmin)
admin.site.register(MenuImage)
=======
admin.site.register(Subscription, SubscriptionAdmin)
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
