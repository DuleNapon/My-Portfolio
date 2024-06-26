# Generated by Django 5.0.3 on 2024-04-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_projects_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='media/testimonials/')),
                ('full_name', models.CharField(max_length=100)),
                ('current_title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('contact', models.URLField(blank=True, null=True)),
                ('testimonial', models.TextField()),
            ],
        ),
    ]
