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
