# Generated by Django 3.0.6 on 2021-01-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0020_auto_20210105_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbooking',
            name='category',
            field=models.CharField(default='Car', max_length=5),
        ),
    ]
