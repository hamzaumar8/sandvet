# Generated by Django 3.0.6 on 2021-01-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0052_remove_hotel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbooking',
            name='category',
            field=models.CharField(default='Hotel', max_length=6),
        ),
    ]
