
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('cart',views.show_cart,name='cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<pk>',views.remove_item_from_cart,name='remove_item'),
    path('checkout',views.checkout_cart,name='checkout'),
    path('orders',views.show_orders,name='orders'),
    path('cart_m',views.cart_m,name='cart_m'),  
    #path('payment',views.payment,name='payment'),  
    path('payment', views.payment, name='payment'),
    #path('process_payment/', views.process_payment, name='process_payment'),
]



