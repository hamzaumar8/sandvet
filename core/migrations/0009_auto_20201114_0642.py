# Generated by Django 3.0.6 on 2020-11-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201113_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
