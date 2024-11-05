from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('about/', views.about, name='about'),
    path('not-found-404/', views.not_found_404, name='not_found_404'),
    path('detail/<slug:slug>/', views.detail_coffeeshop, name='detail_coffeeshop'),
    path('filtered_location/<int:location_id>/', views.filtered_location, name='filtered_location'),
    path('gambar_lowongan/', views.gambar_lowongan, name='gambar_lowongan'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('success/', views.success, name='success'),
    path('map/', views.map_view, name='map'),
    path('contact/', views.contact, name='contact'),
    path('save-visit-status/<int:coffee_shop_id>/<str:status>/', views.save_visit_status, name='save_visit_status'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('contact/', views.contact, name='contact'),
    path('sitemap/', views.sitemap_view, name='sitemap_page'),
]

handler404 = 'aplikasi_tengo.views.not_found_404'
handler500 = 'aplikasi_tengo.views.not_found_500'