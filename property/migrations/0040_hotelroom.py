# Generated by Django 3.0.6 on 2021-01-01 20:13

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import property.models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0039_hotel_bar_or_lounge'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='hotels/')),
                ('description', models.TextField(null=True)),
                ('free_parking', models.BooleanField(default=False)),
                ('housekeeping', models.BooleanField(default=False)),
                ('refrigerator', models.BooleanField(default=False)),
                ('flatscreen_tV', models.BooleanField(default=False)),
                ('kitchenette', models.BooleanField(default=False)),
                ('room_service', models.BooleanField(default=False)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
                ('featured', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', slugify=property.models.custom_slugify, unique_with=('created_at__month',))),
                ('realestate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='property.Hotel')),
            ],
        ),
    ]
