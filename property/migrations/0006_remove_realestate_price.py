# Generated by Django 3.0.6 on 2020-12-25 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_realestate_socialhandle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate',
            name='price',
        ),
    ]
