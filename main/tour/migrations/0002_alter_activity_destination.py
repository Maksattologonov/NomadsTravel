# Generated by Django 4.2.3 on 2024-04-14 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='tour.destination', verbose_name='Пункт'),
        ),
    ]
