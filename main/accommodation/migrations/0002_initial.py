# Generated by Django 4.2.3 on 2025-03-05 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accommodation', '0001_initial'),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.location', verbose_name='Локация'),
        ),
    ]
