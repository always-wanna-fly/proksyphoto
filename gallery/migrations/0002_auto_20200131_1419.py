# Generated by Django 3.0.2 on 2020-01-31 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='price',
        ),
    ]
