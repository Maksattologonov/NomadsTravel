# Generated by Django 4.2.3 on 2024-04-14 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_alter_activity_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='destinations',
        ),
        migrations.AddField(
            model_name='tour',
            name='destinations',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='tour', to='tour.destination', verbose_name='Пункты'),
            preserve_default=False,
        ),
    ]
