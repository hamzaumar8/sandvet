# Generated by Django 3.0.6 on 2020-11-17 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_property_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
    ]
