from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('detail/<int:coffee_shop_id>/', views.detail_coffeeshop, name='detail_coffeeshop'),
]