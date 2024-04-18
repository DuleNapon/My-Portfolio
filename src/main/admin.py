from django.contrib import admin

# Register your models here.
from .models import Certificates, Projects, Testimonials

@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ['get_certificate_name', 'pdf_file', 'jpg_file']

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'industry', 'company', 'link', 'description', 'image']

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['profile_picture', 'full_name', 'current_title', 'company', 'contact', 'testimonial']