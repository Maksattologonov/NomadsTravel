# Generated by Django 4.2.3 on 2025-01-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_remove_tour_location_tour_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='tour_types',
            field=models.ManyToManyField(limit_choices_to={'active': True}, to='tour.typeoftour'),
        ),
    ]
