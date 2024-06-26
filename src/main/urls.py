from django.urls import path
from .views import home_page, cert_galery, project_details
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home_page, name='main'),
    path('certificates/', cert_galery, name='cert'),
    path('project-details/<int:project_id>/', project_details, name='project_details')
] 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

