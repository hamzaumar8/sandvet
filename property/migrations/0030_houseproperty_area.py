# Generated by Django 3.0.6 on 2020-12-31 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0029_auto_20201231_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseproperty',
            name='area',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]