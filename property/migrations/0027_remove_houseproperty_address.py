# Generated by Django 3.0.6 on 2020-12-30 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_auto_20201229_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseproperty',
            name='address',
        ),
    ]
