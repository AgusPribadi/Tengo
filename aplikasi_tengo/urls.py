from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('not-found/', views.not_found, name='not_found'),
    path('detail/<int:coffee_shop_id>/', views.detail_coffeeshop, name='detail_coffeeshop'),
]

handler404 = 'aplikasi_tengo.views.not_found'