# Generated by Django 3.0.6 on 2021-01-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0032_auto_20210101_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='rate',
            field=models.FloatField(default=3),
        ),
    ]