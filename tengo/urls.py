from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from aplikasi_tengo.sitemaps import CoffeeshopSitemap
from aplikasi_tengo.views import RobotsView
from django.views.generic import TemplateView

sitemaps = {
    'coffeeshop': CoffeeshopSitemap,
}

urlpatterns = [
    path('', include('aplikasi_tengo.urls')),
    path("admin/", admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', RobotsView.as_view(), name='robots_file'),
    path('googleb9f5204ada4ff2c8.html', TemplateView.as_view(template_name="googleb9f5204ada4ff2c8.html", content_type="text/html")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)