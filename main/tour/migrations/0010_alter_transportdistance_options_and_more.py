# Generated by Django 4.2.3 on 2025-04-30 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_tourday_total_distance_transportdistance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transportdistance',
            options={'verbose_name': 'Тип транспорта', 'verbose_name_plural': 'Типы транспорта'},
        ),
        migrations.RemoveField(
            model_name='tourday',
            name='car_range',
        ),
        migrations.RemoveField(
            model_name='tourday',
            name='tracking_range',
        ),
        migrations.AlterField(
            model_name='tourday',
            name='total_distance',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6, verbose_name='Общая дистанция'),
        ),
        migrations.AlterField(
            model_name='transportdistance',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Дистанция'),
        ),
        migrations.AlterField(
            model_name='transportdistance',
            name='transport_type',
            field=models.CharField(choices=[('car', 'Машина'), ('walk', 'Пешком'), ('horse', 'Лошадь'), ('ski', 'Лыжи/Борд'), ('boat', 'Лодка'), ('plane', 'Самолет'), ('helicopter', 'Вертолет'), ('train', 'Поезд')], max_length=10, verbose_name='Тип транспорта'),
        ),
    ]
