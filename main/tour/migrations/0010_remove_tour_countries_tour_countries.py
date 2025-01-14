# Generated by Django 4.2.3 on 2025-01-05 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_tour_tour_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='countries',
        ),
        migrations.AddField(
            model_name='tour',
            name='countries',
            field=models.ForeignKey(default=2, limit_choices_to={'type__in': ['country']}, on_delete=django.db.models.deletion.CASCADE, to='tour.location'),
            preserve_default=False,
        ),
    ]
