from django.urls import path
from .views import home_page,cert_galery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page, name='main'),
    path('certificates/', cert_galery, name='cert')
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)