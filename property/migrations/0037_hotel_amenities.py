# Generated by Django 3.0.6 on 2021-01-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0036_auto_20210101_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='amenities',
            field=models.TextField(blank=True, null=True),
        ),
    ]
