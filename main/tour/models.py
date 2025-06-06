import requests
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta
from accommodation.models import Accommodation
from categories.models import Category, Health, Visa, Gear, Includes, Excludes, Meal, Entertainment
from user.models import CustomUser
from .managers import Location
from django.conf import settings


class Booking(models.Model):
    BOOK_STATUS = [
        ('paid', 'paid'),
        ('booked', 'booked'),
        ('conditionally', 'conditionally'),
    ]
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='bookings',
                                      verbose_name=_('Размещение'))
    # user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    check_in = models.DateField(verbose_name=_('Дата заезда'))
    check_out = models.DateField(verbose_name=_('Дата выезда'))
    status = models.CharField(max_length=13, choices=BOOK_STATUS, verbose_name=_('Статус'))

    class Meta:
        verbose_name = _('Бронирование')
        verbose_name_plural = _('Бронирования')


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name=_("Локация"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class CityImage(models.Model):
    city_id = models.ForeignKey('City', on_delete=models.DO_NOTHING, verbose_name=_('Город'))
    image = models.ImageField(upload_to='cities', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'city_images'
        verbose_name = 'Изображение города'
        verbose_name_plural = 'Изображение городов'


class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name=_("Локация"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'regions'
        verbose_name = 'Область'
        verbose_name_plural = 'Области'


class RegionImage(models.Model):
    region_id = models.ForeignKey('Region', on_delete=models.DO_NOTHING, verbose_name=_('Регион'))
    image = models.ImageField(upload_to='regions', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'region_images'
        verbose_name = 'Изображение региона'
        verbose_name_plural = 'Изображение регионов'


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name=_("Локация"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'countries'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class CountryImage(models.Model):
    country_id = models.ForeignKey('Country', on_delete=models.DO_NOTHING, verbose_name=_('Страна'))
    image = models.ImageField(upload_to='countries', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'country_images'
        verbose_name = 'Изображение страны'
        verbose_name_plural = 'Изображение стран'


class TypeOfTour(models.Model):
    type = models.CharField(max_length=100, verbose_name=_("Тип"))
    icon = models.FileField(upload_to='icons', null=True, verbose_name=_("Иконка"))

    def __str__(self):
        return self.type

    class Meta:
        db_table = "level_of tour"
        verbose_name = 'Тип Тура'
        verbose_name_plural = 'Типы Туров'


class DestinationImages(models.Model):
    destination_id = models.ForeignKey('Destination', related_name='destination_image', on_delete=models.DO_NOTHING,
                                       verbose_name=_('Страна'))
    image = models.ImageField(upload_to='destination/', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'destination_images'
        verbose_name = 'Изображение пункта'
        verbose_name_plural = 'Изображение пунктов'


class Destination(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_("Описание"))
    main_image = models.ImageField(upload_to='destination/', verbose_name=_("Главное изображение"))
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name=_("Локация"))
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_("Регион"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Категория"))
    active = models.BooleanField(default=True, verbose_name=_("Активный"))

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = 'destination'
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class DestinationRating(models.Model):
    destination = models.ForeignKey('Destination', related_name='ratings', on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name=_('Рейтинг'), max_digits=2, decimal_places=1)

    def __str__(self):
        return self.destination.title + str(self.value)

    class Meta:
        db_table = 'destination_rating'
        verbose_name = 'Рейтинг пункта'
        verbose_name_plural = 'Рейтинги пунктов'


class Tour(models.Model):
    TYPE_OF_DIFFICULTY = [
        ('1', 'Легкий'),
        ('2', 'Средний'),
        ('3', 'Сложный'),
    ]

    TYPE_OF_VISA_INFO = [
        ('электронная', 'Электронная виза'),
        ('обыкновенная ', 'Обыкновенная  виза'),
        ('транзитная', 'Транзитная виза'),
        ('временная', 'Виза временно проживающего лица'),
    ]
    name = models.CharField(max_length=255, verbose_name=_('Название тура'))
    price = models.PositiveIntegerField(verbose_name=_("Цена"))
    promotion = models.PositiveSmallIntegerField(default=0, verbose_name=_("Скидка"),
                                                 help_text='Указывайте в дробном виде 0.1')
    countries = models.ManyToManyField(to=Location, limit_choices_to={'type__in': ['country']})
    description = models.TextField(verbose_name=_("Описание"))
    date_start = models.DateTimeField(verbose_name=_("Дата начала"))
    duration = models.CharField(max_length=255, verbose_name=_("Длительность"))
    tour_types = models.ManyToManyField(to=TypeOfTour, blank=True)
    difficulty = models.CharField(choices=TYPE_OF_DIFFICULTY, max_length=20, verbose_name=_("Сложность"))
    total_distance = models.FloatField(verbose_name=_("Итоговая дистанция"), blank=True)
    visa_information = models.CharField(choices=TYPE_OF_VISA_INFO, max_length=255,
                                        verbose_name=_("Информация о визе"))
    health_information = models.ManyToManyField(to=Health,
                                                verbose_name=_("Информация о здоровье"), blank=True)
    notes = models.TextField(verbose_name=_("Примечания"), null=True, blank=True)
    video = models.URLField(verbose_name=_("Ссылка на видео"), null=True, blank=True)
    map = models.URLField(verbose_name=_("Ссылка на карту"), null=True, blank=True)
    main_image = models.ImageField(upload_to="tour/", verbose_name=_("Главное изображение"))
    personal_gear = models.ManyToManyField(to=Gear, verbose_name=_("Снаряжение"), blank=True)
    includes = models.ManyToManyField(to=Includes, verbose_name=_("Включения"), blank=True)
    excludes = models.ManyToManyField(to=Excludes, verbose_name=_("Исключения"), blank=True)
    days = models.ManyToManyField('TourDay', through='TourDayOrder', related_name='tours')

    def __str__(self):
        return self.name

    @property
    def geomap_longitude(self):
        return self.countries if self.countries else None

    @property
    def geomap_latitude(self):
        return self.countries if self.countries else None

    class Meta:
        db_table = "tour"
        verbose_name = _("Тур")
        verbose_name_plural = _("Туры")


class TourPhotos(models.Model):
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name=_('Тур'))
    image = models.ImageField(upload_to='commentImages', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'tour_images'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class TourDayOrder(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name=_('Тур'))
    tour_day = models.ForeignKey('TourDay', verbose_name=_('День тура'), on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField(verbose_name="Номер дня")

    class Meta:
        ordering = ['day_number']
        unique_together = ('tour', 'day_number')
        verbose_name = 'День тура'
        verbose_name_plural = 'Дни тура'

    def __str__(self):
        return "Выбрать"


class TourDay(models.Model):

    name = models.CharField(verbose_name=_("Наименование"), max_length=255)
    # locations = models.ManyToManyField(Location, verbose_name=_("Локации"))
    destination = models.ManyToManyField(Destination, verbose_name=_('Пункты'))
    description = models.TextField(verbose_name=_("Описание"), null=True)
    total_distance = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name=_("Общая дистанция"), editable=False)
    main_image = models.ImageField(upload_to="tour/", verbose_name=_("Главное изображение"), null=True)
    height_difference = models.CharField(verbose_name=_('Перепад высоты'), max_length=255, null=True)
    weather = models.CharField(verbose_name=_('Погода'), max_length=255, null=True, blank=True)
    weather_date = models.DateField(verbose_name=_('Дата погоды'), null=True, blank=True)
    meals = models.ManyToManyField(Meal, verbose_name=_("Питание"), max_length=50, blank=False, related_name='tour_meals')
    accommodation = models.ManyToManyField(to=Accommodation, related_name='accommodation',
                                           verbose_name=_("Проживание"), blank=True)
    entertainment = models.ManyToManyField(to='Activity', verbose_name=_("Развлечения"), blank=True,
                                           related_name='entertainment')
    details = models.TextField(verbose_name=_("Детали"), null=True, blank=True)

    class Meta:
        db_table = 'tour_day'
        verbose_name = _("День тура")
        verbose_name_plural = _("Дни тура")

    def __str__(self):
        return self.name

    def update_total_distance(self):
        total = sum(d.distance for d in self.distances.all())
        self.total_distance = total
        self.save(update_fields=['total_distance'])

    def fetch_weather(self):
        destination = self.destination.first()
        if not destination:
            self.weather = "Нет пункта назначения"
            self.save()
            return

        api_key = settings.OPEN_WEATHER_MAP_TOKEN
        date = self.weather_date or (datetime.now().date() + timedelta(days=1))
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={destination.location.lat}&lon={destination.location.lon}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            forecast = self.find_forecast_for_date(data['list'], date)
            if forecast:
                temp = forecast['main']['temp']
                description = forecast['weather'][0]['description']
                self.weather = f"{temp}°C, {description}"
            else:
                self.weather = "Нет данных для этой даты"
        else:
            self.weather = "Ошибка получения погоды"

        self.save()

    def find_forecast_for_date(self, forecasts, target_date):
        for forecast in forecasts:
            forecast_date = forecast['dt_txt'].split(' ')[0]  # Формат даты
            if forecast_date == str(target_date):
                return forecast
        return None


class TransportDistance(models.Model):
    TRANSPORT_CHOICES = [
        ('car', 'Машина'),
        ('walk', 'Пешком'),
        ('horse', 'Лошадь'),
        ('ski', 'Лыжи/Борд'),
        ('boat', 'Лодка'),
        ('plane', 'Самолет'),
        ('helicopter', 'Вертолет'),
        ('train', 'Поезд'),
    ]

    tour_day = models.ForeignKey(TourDay, related_name='distances', on_delete=models.CASCADE)
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES, verbose_name=_("Тип транспорта"))
    distance = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Дистанция"))

    class Meta:
        verbose_name = _("Тип транспорта")
        verbose_name_plural = _("Типы транспорта")

    def __str__(self):
        return self.transport_type



class Itinerary(models.Model):
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name=_('Тур'))
    date = models.DateField(verbose_name=_("Дата"), null=False)
    title = models.CharField(verbose_name=_("Заголовок"), max_length=255)
    meals = models.ManyToManyField(Meal, related_name='itenerary_meal', verbose_name=_("Еда"))
    accommodation = models.ForeignKey(Accommodation, on_delete=models.DO_NOTHING, verbose_name=_("Проживание"))
    entertainment = models.ForeignKey(Entertainment, on_delete=models.DO_NOTHING, verbose_name=_("Развлечения"))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'itinerary'
        verbose_name = _('Маршрут')
        verbose_name_plural = _('Маршруты')


class TourComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    tour_id = models.ForeignKey(Tour, verbose_name=_('Тур'), on_delete=models.CASCADE)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.created_at}'

    class Meta:
        db_table = 'tour_comments'
        verbose_name = _("Комментарий к туру")
        verbose_name_plural = _("Комментарии к туру")


class TourCommentPhotos(models.Model):
    comment_id = models.ForeignKey(TourComment, on_delete=models.DO_NOTHING, verbose_name=_('Комментарий'))
    image = models.ImageField(upload_to='commentImages', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'comment_images'
        verbose_name = 'Изображение комментария'
        verbose_name_plural = 'Изображения комментариев'


class TourRating(models.Model):
    tour_id = models.ForeignKey(Tour, verbose_name=_("Тур"), on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(verbose_name=_("Рейтинг"),
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Пользователь"))

    def __str__(self):
        return f"{self.tour_id}, Пользователь: {self.user.email}, Рейтиинг: {self.rating}"

    class Meta:
        db_table = 'tour_rating'
        verbose_name = 'Рейтинг тура'
        verbose_name_plural = 'Рейтинги туров'


class Activity(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

    @property
    def geomap_longitude(self):
        return  None

    @property
    def geomap_latitude(self):
        return None

    class Meta:
        db_table = 'activity'
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'


class ActivityImage(models.Model):
    activity_id = models.ForeignKey(Activity, verbose_name=_('Активность'), related_name='activity_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='commentImages', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'activity_images'
        verbose_name = 'Изображение активности'
        verbose_name_plural = 'Изображения активностей'