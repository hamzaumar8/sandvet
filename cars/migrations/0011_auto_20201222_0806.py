# Generated by Django 3.0.6 on 2020-12-22 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20201222_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='SparePartImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='cars/spareparts')),
                ('sparepart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sparepartimages', to='cars.SparePart')),
            ],
        ),
        migrations.DeleteModel(
            name='Sparemage',
        ),
    ]