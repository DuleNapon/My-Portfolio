# Generated by Django 5.0.3 on 2024-04-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/project_images/')),
                ('project_type', models.CharField(choices=[('Agile', 'Agile'), ('Waterfall', 'Waterfall'), ('Learning', 'Learning'), ('Other', 'Other')], default='Other', max_length=20)),
                ('industry', models.CharField(choices=[('Automotive', 'Automotive'), ('IT', 'IT'), ('Rolling stock', 'Rolling stock'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], default='Other', max_length=30)),
                ('link', models.URLField()),
            ],
        ),
    ]
