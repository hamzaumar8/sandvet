# Generated by Django 3.0.6 on 2020-12-26 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0021_auto_20201226_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='address',
            new_name='location_address',
        ),
    ]
