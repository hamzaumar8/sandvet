# Generated by Django 3.0.6 on 2021-01-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0055_auto_20210109_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroombooking',
            name='check_in',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='hotelroombooking',
            name='check_out',
            field=models.DateTimeField(null=True),
        ),
    ]
