from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Certificates

@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ['get_certificate_name', 'pdf_file', 'jpg_file']
