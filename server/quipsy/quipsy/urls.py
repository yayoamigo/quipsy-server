
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('djoser.urls')), # djoser
    path('api/v1', include('djoser.urls.authtoken')), # djoser
    path('api/v1/', include('product.urls')), # product
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media
