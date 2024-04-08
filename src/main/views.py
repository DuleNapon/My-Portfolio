from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, "HomePage/main.html")

def cert_galery(request):
    return render(request, "HomePage/galery_cert.html")