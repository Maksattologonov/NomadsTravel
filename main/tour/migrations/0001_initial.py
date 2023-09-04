# Generated by Django 4.2.3 on 2023-08-30 15:17

from django.db import migrations, models
import django.db.models.deletion
import django_admin_geomap


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название отели')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
                'db_table': 'accommodations',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название локации')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('lat', models.FloatField(verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
                'db_table': 'locations',
            },
            bases=(models.Model, django_admin_geomap.GeoItem),
        ),
        migrations.CreateModel(
            name='RatingAccommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.country')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.location', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Области',
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='RegionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='regions', verbose_name='Загрузить изображение')),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Изображение региона',
                'verbose_name_plural': 'Изображение регионов',
                'db_table': 'region_images',
            },
        ),
        migrations.CreateModel(
            name='CountryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='countries', verbose_name='Загрузить изображение')),
                ('Country_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.country', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Изображение страны',
                'verbose_name_plural': 'Изображение стран',
                'db_table': 'country_images',
            },
        ),
        migrations.AddField(
            model_name='country',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.location', verbose_name='Локация'),
        ),
        migrations.CreateModel(
            name='CityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cities', verbose_name='Загрузить изображение')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Изображение города',
                'verbose_name_plural': 'Изображение городов',
                'db_table': 'city_images',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.location', verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.region'),
        ),
        migrations.CreateModel(
            name='AccommodationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='accommodations', verbose_name='Загрузить изображение')),
                ('accommodation_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.accommodation', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Изображение отеля',
                'verbose_name_plural': 'Изображение отелей',
                'db_table': 'accommodation_images',
            },
        ),
        migrations.AddField(
            model_name='accommodation',
            name='city',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.DO_NOTHING, to='tour.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='location',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.DO_NOTHING, to='tour.location', verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.ratingaccommodation', verbose_name='Рейтинг'),
        ),
    ]
