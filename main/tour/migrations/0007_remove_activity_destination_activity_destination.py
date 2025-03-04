# Generated by Django 4.2.3 on 2025-03-04 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_remove_activity_destination_alter_activity_icon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='destination',
        ),
        migrations.AddField(
            model_name='activity',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='tour.destination', verbose_name='Пункт'),
            preserve_default=False,
        ),
    ]
