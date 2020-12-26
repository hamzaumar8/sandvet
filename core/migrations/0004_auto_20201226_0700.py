# Generated by Django 3.0.6 on 2020-12-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201224_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='region',
            field=models.CharField(blank=True, choices=[('ashanti', 'Ashanti'), ('ahafo', 'Ahafo'), ('brong-ahafo', 'Brong Ahafo'), ('bono-east', 'Bono East '), ('central', 'Central'), ('eastern', 'Eastern'), ('greater-accra', 'Greater Accra'), ('northern', 'Northern'), ('savannah', 'Savannah'), ('north-east', 'North East'), ('upper-east', 'Upper East'), ('upper-west', 'Upper West'), ('volta', 'Volta'), ('oti', 'Oti Region'), ('werstern', 'Western'), ('werstern-north', 'Western North')], max_length=20, null=True, unique=True),
        ),
    ]
