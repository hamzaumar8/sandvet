# Generated by Django 3.0.6 on 2020-12-14 16:43

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import property.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, null=True)),
                ('purpose', models.CharField(choices=[('sale', 'for sale'), ('rent', 'for rent')], default='sale', max_length=4)),
                ('bed', models.PositiveIntegerField(default=1)),
                ('from_price', models.FloatField(null=True)),
                ('to_price', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.Category')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Locality')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField()),
                ('purpose', models.CharField(choices=[('sale', 'sale'), ('rent', 'rent')], default='sale', max_length=4)),
                ('region', models.CharField(blank=True, choices=[('ashanti', 'Ashanti'), ('ahafo', 'Ahafo'), ('brong-ahafo', 'Brong Ahafo'), ('bono-east', 'Bono East '), ('central', 'Central'), ('eastern', 'Eastern'), ('greater-accra', 'Greater Accra'), ('northern', 'Northern'), ('savannah', 'Savannah'), ('north-east', 'North East'), ('upper-east', 'Upper East'), ('upper-west', 'Upper West'), ('volta', 'Volta'), ('oti', 'Oti Region'), ('werstern', 'Western'), ('werstern-north', 'Western North')], max_length=20, null=True)),
                ('image', models.ImageField(upload_to='property/')),
                ('description', models.TextField(null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('featured', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', slugify=property.models.custom_slugify, unique_with=('created_at__month',))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Category')),
            ],
        ),
        migrations.CreateModel(
            name='LandProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('dimension', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Locality')),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='landproperty', to='property.Property')),
            ],
        ),
        migrations.CreateModel(
            name='HouseProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('bed', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('bath', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('garage', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Locality')),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='houseproperty', to='property.Property')),
            ],
        ),
    ]
