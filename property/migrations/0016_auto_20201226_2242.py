# Generated by Django 3.0.6 on 2020-12-26 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_realestate_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseproperty',
            name='property',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houseproperty', to='property.Property'),
        ),
    ]
