# Generated by Django 5.0.7 on 2024-09-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_tool'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='year',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]