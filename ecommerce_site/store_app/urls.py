from django.urls import path

from . import views

urlpatterns = [
    path('',views.e_store,name="store"),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout')
]
