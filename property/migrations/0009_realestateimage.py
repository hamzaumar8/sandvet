# Generated by Django 3.0.6 on 2020-12-25 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20201225_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstateImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='realestate/imgs/')),
                ('realestate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realestateimages', to='property.RealEstate')),
            ],
        ),
    ]
