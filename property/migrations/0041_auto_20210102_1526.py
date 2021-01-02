# Generated by Django 3.0.6 on 2021-01-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0040_hotelroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelroom',
            old_name='flatscreen_tV',
            new_name='flatscreen_tv',
        ),
        migrations.RemoveField(
            model_name='hotelroom',
            name='free_parking',
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='price',
            field=models.FloatField(default=100.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotelroom',
            name='image',
            field=models.ImageField(upload_to='hotels/rooms/'),
        ),
    ]