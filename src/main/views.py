from django.shortcuts import render
from django.http import HttpResponse
from .models import Certificates

# Create your views here.

def home_page(request):
    # Retrieve all certificates from the database
    certificates = Certificates.objects.all()
    # Pass the certificates to the template context
    context = {'certificates': certificates}
    return render(request, "HomePage/main.html", context)

def cert_galery(request):
    # Retrieve all certificates from the database
    certificates = Certificates.objects.all()
    # Pass the certificates to the template context
    context = {'certificates': certificates}
    return render(request, "HomePage/galery_cert.html", context)

