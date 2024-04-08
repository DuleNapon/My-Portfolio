from django.urls import path
from .views import home_page,cert_galery

urlpatterns = [
    path('', home_page, name='main'),
    path('certificates/', cert_galery, name='cert')
]
