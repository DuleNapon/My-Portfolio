from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Certificates, Projects
from django.shortcuts import redirect
# Create your views here.

def home_page(request):
    # Retrieve all certificates from the database
    certificates = Certificates.objects.all()
    # Retrieve all projects from the database
    projects = Projects.objects.all()
    # Pass the certificates and projects to the template context
    context = {'certificates': certificates, 'projects': projects}
    return render(request, "HomePage/main.html", context)

def cert_galery(request):
    # Retrieve all certificates from the database
    certificates = Certificates.objects.all()
    # Pass the certificates to the template context
    context = {'certificates': certificates}
    return render(request, "HomePage/galery_cert.html", context)

def project_details(request, project_id):
    # Retrieve all projects from the database
    project = get_object_or_404(Projects, pk=project_id)
    # Pass the project to the template context
    return render(request, "HomePage/project_details.html", {'project': project})