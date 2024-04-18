from django.db import models

# Create your models here.

class Certificates(models.Model):
    # Field to store PDF file
    pdf_file = models.FileField(upload_to='media/certificates/pdf')

    # Field to store JPG file
    jpg_file = models.ImageField(upload_to='media/certificates/jpg')

    def get_certificate_name(self):
        # Extract file name from PDF file path
        pdf_file_name = self.pdf_file.name

        # Split file name by '/' and get the last part
        file_name_parts = pdf_file_name.split('/')
        file_name = file_name_parts[-1]

        # Remove file extension to get certificate name
        certificate_name = file_name.split('.')[0]

        # Replace underscores with spaces in the certificate name
        certificate_name = certificate_name.replace('_', ' ')

        return certificate_name

    def __str__(self):
        return self.get_certificate_name()

class Projects(models.Model):
    PROJECT_TYPES = [
        ('Agile', 'Agile'),
        ('Waterfall', 'Waterfall'),
        ('Learning', 'Learning'),
        ('Other', 'Other'),
    ]

    INDUSTRIES = [
        ('Automotive', 'Automotive'),
        ('IT', 'IT'),
        ('Rolling stock', 'Rolling stock'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]
    

    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100, default='N/A')
    image = models.ImageField(upload_to='media/project_images/')
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='Other')
    industry = models.CharField(max_length=30, choices=INDUSTRIES, default='Other')
    link = models.URLField()

    def __str__(self):
        return self.title

class Testimonials(models.Model):
    profile_picture = models.ImageField(upload_to='media/testimonials/', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    current_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    contact = models.URLField(null=True, blank=True)
    testimonial = models.TextField()

    def __str__(self):
        return self.full_name