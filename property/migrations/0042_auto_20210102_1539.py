# Generated by Django 3.0.6 on 2021-01-02 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0041_auto_20210102_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelroom',
            old_name='realestate',
            new_name='hotel',
        ),
    ]
