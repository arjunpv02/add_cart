from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path("seller_dashboard",views.seller_dashboard,name='seller_dashboard'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)