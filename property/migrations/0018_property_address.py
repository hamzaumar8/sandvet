# Generated by Django 3.0.6 on 2020-12-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20201226_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
