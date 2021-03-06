# Generated by Django 3.0.6 on 2020-12-20 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20201215_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpareImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='cars/spareparts')),
                ('sparepart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spareimages', to='cars.Car')),
            ],
        ),
    ]
