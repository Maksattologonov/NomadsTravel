# Generated by Django 5.0.3 on 2024-03-29 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_remove_tour_excludes_remove_tour_health_information_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='level',
        ),
    ]