# Generated by Django 3.0.6 on 2020-11-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_auto_20201121_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='bed',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='from_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='to_price',
            field=models.FloatField(null=True),
        ),
    ]