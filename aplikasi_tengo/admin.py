from django.contrib import admin
from .models import (
    CoffeeShop, CoffeeShopTag, CoffeeShopImage, GambarLowongan, 
    Subscription, Lokasi, Fasilitas, Recommendation, VisitStatus,
    MenuImage, PaymentMethod
)
from django.http import HttpResponse
import csv

class CoffeeShopImageInline(admin.TabularInline):
    model = CoffeeShopImage
    extra = 1

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
        'lokasi', 'fasilitas', 'metode_pembayaran'  # Tambahkan metode_pembayaran
    ]

    def download_data_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="coffee_shops.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Nomor', 'Nama', 'Alamat', 'Jam Buka', 'Kontak', 
            'Instagram URL', 'TikTok URL', 'Google Maps URL', 
            'Menu', 'Latitude', 'Longitude', 'Metode Pembayaran'  # Tambahkan kolom metode_pembayaran
        ])

        for index, coffee_shop in enumerate(queryset, start=1):
            metode_pembayaran = ', '.join([metode.nama_metode for metode in coffee_shop.metode_pembayaran.all()])
            writer.writerow([
                index, 
                coffee_shop.nama, 
                coffee_shop.alamat, 
                coffee_shop.jam_buka, 
                coffee_shop.contact,
                coffee_shop.instagram_url, 
                coffee_shop.tiktok_url, 
                coffee_shop.google_maps_url,
                coffee_shop.menu_images,
                coffee_shop.latitude,
                coffee_shop.longitude,
                metode_pembayaran  # Menyimpan metode pembayaran dalam CSV
            ])

        return response

    download_data_as_csv.short_description = 'Download Data as CSV'

class FasilitasAdmin(admin.ModelAdmin):
    list_display = ['nama_fasilitas']

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']

class VisitStatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'coffee_shop', 'status']
    list_filter = ['status', 'user']

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['nama_metode']

admin.site.register(CoffeeShop, CoffeeShopAdmin)
admin.site.register(GambarLowongan)
admin.site.register(CoffeeShopTag)
admin.site.register(Lokasi)
admin.site.register(Recommendation)
admin.site.register(Fasilitas, FasilitasAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(VisitStatus, VisitStatusAdmin)
admin.site.register(MenuImage)
admin.site.register(PaymentMethod, PaymentMethodAdmin)