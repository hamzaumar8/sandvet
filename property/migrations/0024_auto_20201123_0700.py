# Generated by Django 3.0.6 on 2020-11-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0023_property_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='featured',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]