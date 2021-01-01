# Generated by Django 3.0.6 on 2021-01-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0031_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='purpose',
        ),
        migrations.AddField(
            model_name='hotel',
            name='logo',
            field=models.ImageField(null=True, upload_to='hotels/logo'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(upload_to='hotels/'),
        ),
    ]