from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
=======
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
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
<<<<<<< HEAD
    path('map/', views.map_view, name='map'),
    path('save-visit-status/<int:coffee_shop_id>/<str:status>/', views.save_visit_status, name='save_visit_status'),
]

handler404 = 'aplikasi_tengo.views.not_found'
=======
]

handler404 = 'aplikasi_tengo.views.not_found'
>>>>>>> 92ba82aacc09e0f64eecc1a10351825e7d9550a1
