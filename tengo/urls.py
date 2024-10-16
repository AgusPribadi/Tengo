from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from aplikasi_tengo.sitemaps import CoffeeshopSitemap

sitemaps = {
    'coffeeshop': CoffeeshopSitemap,
}

urlpatterns = [
    path('', include('aplikasi_tengo.urls')),
    path("admin/", admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)