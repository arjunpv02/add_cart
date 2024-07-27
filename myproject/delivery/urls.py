from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("delivery_dashboard",views.delivery_dashboard,name='delivery_dashboard'),
    path('delivery/edit/<int:delivery_id>/', views.edit_delivery, name='edit_delivery'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)