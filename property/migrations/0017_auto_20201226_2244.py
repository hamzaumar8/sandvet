# Generated by Django 3.0.6 on 2020-12-26 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20201226_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landproperty',
            name='property',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='landproperty', to='property.Property'),
        ),
    ]