
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('account',views.show_account,name='account'),
    path('logout',views.sign_out,name="logout"),
]



