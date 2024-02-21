from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('not-found/', views.not_found, name='not_found'),
    path('detail/<slug:slug>/', views.detail_coffeeshop, name='detail_coffeeshop'),
    path('filtered_location/<int:location_id>/', views.filtered_location, name='filtered_location'),
    path('gambar_lowongan/', views.gambar_lowongan, name='gambar_lowongan'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('success/', views.success, name='success'),
]

handler404 = 'aplikasi_tengo.views.not_found'