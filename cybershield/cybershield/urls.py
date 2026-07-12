from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# డెవలప్‌మెంట్ మోడ్‌లో (DEBUG=True) ఉన్నప్పుడు స్టాటిక్ ఫైల్స్ లోడ్ అవ్వడానికి ఇది తప్పనిసరి
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
