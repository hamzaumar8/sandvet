# Generated by Django 3.0.6 on 2021-01-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0038_auto_20210102_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='bar_or_lounge',
            field=models.BooleanField(default=False),
        ),
    ]