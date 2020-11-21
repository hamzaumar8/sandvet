# Generated by Django 3.0.6 on 2020-11-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20201120_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='purpose',
            field=models.CharField(choices=[('', ''), ('sale', 'for sale'), ('rent', 'for rent')], default='sale', max_length=4),
        ),
    ]
