from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Certificates, Projects, Testimonials, Roadmap
from django.shortcuts import redirect
# Create your views here.

def home_page(request):
    # Retrieve all certificates from the database, sorted alphabetically by file name
    certificates = Certificates.objects.all().order_by('pdf_file')
    # Retrieve all projects from the database
    projects = Projects.objects.all()
    # Retrieve all testimonials from the database
    testimonials = Testimonials.objects.all()
    # Retrieve the roadmap configuration
    roadmap = Roadmap.objects.first()
    # Pass the certificates, projects, testimonials, and roadmap to the template context
    context = {
        'certificates': certificates,
        'projects': projects,
        'testimonials': testimonials,
        'roadmap': roadmap,
    }
    return render(request, "HomePage/main.html", context)


def cert_galery(request):
    # Retrieve all certificates from the database, sorted alphabetically by file name
    certificates = Certificates.objects.all().order_by('pdf_file')
    # Pass the certificates to the template context
    context = {'certificates': certificates}
    return render(request, "HomePage/galery_cert.html", context)

def project_details(request, project_id):
    # Retrieve all projects from the database
    project = get_object_or_404(Projects, pk=project_id)
    # Pass the project to the template context
    return render(request, "HomePage/project_details.html", {'project': project})