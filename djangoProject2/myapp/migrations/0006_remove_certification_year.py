# Generated by Django 5.0.7 on 2024-09-01 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_certification_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certification',
            name='year',
        ),
    ]