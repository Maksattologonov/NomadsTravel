# Generated by Django 4.2.3 on 2025-01-02 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_remove_tourday_meals_tourday_meals'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='location',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='tour.location'),
            preserve_default=False,
        ),
    ]
