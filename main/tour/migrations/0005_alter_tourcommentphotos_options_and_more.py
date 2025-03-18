# Generated by Django 4.2.3 on 2025-03-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_remove_activity_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tourcommentphotos',
            options={'verbose_name': 'Изображение комментария', 'verbose_name_plural': 'Изображения комментариев'},
        ),
        migrations.RemoveField(
            model_name='activity',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='tourday',
            name='tour',
        ),
        migrations.CreateModel(
            name='TourDayOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.PositiveIntegerField(verbose_name='Номер дня')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
                ('tour_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tourday')),
            ],
            options={
                'ordering': ['day_number'],
                'unique_together': {('tour', 'day_number')},
            },
        ),
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='commentImages', verbose_name='Загрузить изображение')),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_images', to='tour.activity', verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Изображение активности',
                'verbose_name_plural': 'Изображения активностей',
                'db_table': 'activity_images',
            },
        ),
        migrations.AddField(
            model_name='tour',
            name='days',
            field=models.ManyToManyField(related_name='tours', through='tour.TourDayOrder', to='tour.tourday'),
        ),
    ]
