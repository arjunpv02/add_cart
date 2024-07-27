
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('product_list',views.list_product,name='list_product'),
    path('product_detail/<pk>' , views.detail_product, name='detail_product'),
]


#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



#path('admin/', admin.site.urls),
#path('',include('products.urls')),