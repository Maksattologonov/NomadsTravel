# Generated by Django 5.0.3 on 2024-04-16 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0001_initial'),
        ('tour', '0004_remove_tour_geomap_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='city',
        ),
        migrations.RemoveField(
            model_name='accommodation',
            name='location',
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accommodation.accommodation', verbose_name='Проживание'),
        ),
        migrations.RemoveField(
            model_name='accommodationrating',
            name='target_content_type',
        ),
        migrations.AlterField(
            model_name='booking',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='accommodation.accommodation', verbose_name='Размещение'),
        ),
        migrations.DeleteModel(
            name='AccommodationImage',
        ),
        migrations.DeleteModel(
            name='AccommodationRating',
        ),
        migrations.DeleteModel(
            name='Accommodation',
        ),
    ]
