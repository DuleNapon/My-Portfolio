# Generated by Django 5.0.3 on 2024-04-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='company',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]