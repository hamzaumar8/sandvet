# Generated by Django 3.0.6 on 2021-01-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0056_auto_20210109_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroombooking',
            name='check_out',
            field=models.DateField(null=True),
        ),
    ]
