# Generated by Django 3.0.6 on 2020-12-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_auto_20201222_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
