from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('property/', include('property.urls', namespace='property')),
    path('cars/', include('cars.urls', namespace='cars')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)