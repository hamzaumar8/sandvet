# Generated by Django 3.0.6 on 2020-11-17 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20201117_0714'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='type',
            new_name='category',
        ),
    ]