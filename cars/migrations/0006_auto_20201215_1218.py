# Generated by Django 3.0.6 on 2020-12-15 20:18

import autoslug.fields
import cars.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201215_0344'),
        ('cars', '0005_brand_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='purpose',
            field=models.CharField(blank=True, choices=[('sale', 'Sale'), ('hire', 'Hire')], max_length=4, null=True),
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='spareparts/')),
                ('description', models.TextField(null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('featured', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', slugify=cars.models.custom_slugify, unique_with=('created_at__month',))),
                ('region', models.CharField(blank=True, choices=[('ashanti', 'Ashanti'), ('ahafo', 'Ahafo'), ('brong-ahafo', 'Brong Ahafo'), ('bono-east', 'Bono East '), ('central', 'Central'), ('eastern', 'Eastern'), ('greater-accra', 'Greater Accra'), ('northern', 'Northern'), ('savannah', 'Savannah'), ('north-east', 'North East'), ('upper-east', 'Upper East'), ('upper-west', 'Upper West'), ('volta', 'Volta'), ('oti', 'Oti Region'), ('werstern', 'Western'), ('werstern-north', 'Western North')], max_length=20, null=True)),
                ('state', models.CharField(choices=[('new', 'New'), ('used', 'Used')], max_length=4, null=True)),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sparelocality', to='core.Locality')),
            ],
        ),
    ]
