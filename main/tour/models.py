from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accommodation.models import Accommodation
from categories.models import Category, Health, Visa, Gear, Includes, Excludes, Meal, Entertainment
from user.models import CustomUser
from .managers import Location


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

    def __str__(self):
        return self.type

    class Meta:
        db_table = "type_of tour"
        verbose_name = 'Тип Тура'
        verbose_name_plural = 'Типы Туров'


class DestinationImages(models.Model):
    destination_id = models.ForeignKey('Destination', on_delete=models.DO_NOTHING, verbose_name=_('Страна'))
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
    weather = models.CharField(verbose_name=_("Погода"), max_length=255)

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = 'destination'
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class DestinationRating(models.Model):
    destination = models.ForeignKey('Destination',  related_name='ratings', on_delete=models.CASCADE)
    value = models.DecimalField(verbose_name=_('Рейтинг'), max_digits=2, decimal_places=1)

    def __str__(self):
        return self.destination.title + str(self.value)

    class Meta:
        db_table = 'destination_rating'
        verbose_name = 'Рейтинг пункта'
        verbose_name_plural = 'Рейтинги пунктов'


class Tour(models.Model):
    TOUR_LEVEL = [
        ("Easy", "easy"),
        ("Medium", "medium"),
        ("Hard", "hard"),
    ]

    title = models.CharField(max_length=255, verbose_name=_('Название тура'))
    price = models.PositiveIntegerField(verbose_name=_("Цена"))
    description = models.TextField(verbose_name=_("Описание"))
    date_start = models.DateTimeField(verbose_name=_("Дата начала"))
    duration_date = models.CharField(max_length=255, verbose_name=_("Длительность"))
    destinations = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="tour", verbose_name=_("Пункты"))
    # level = models.CharField(choices=TOUR_LEVEL, max_length=25, verbose_name=_("Сложность"))
    type_of = models.ManyToManyField(to=TypeOfTour, verbose_name=_("Сложность"))
    distance = models.FloatField(verbose_name=_("Дистанция"))
    altitude = models.CharField(max_length=255, verbose_name=_("Перепад высоты"))
    visa_information = models.ManyToManyField(to=Visa,
                                              verbose_name=_("Информация о визе"))
    health_information = models.ManyToManyField(to=Health,
                                                verbose_name=_("Информация о здоровье"))
    weather = models.CharField(verbose_name=_("Погода"), max_length=255)
    notes = models.TextField(verbose_name=_("Примечания"))
    video = models.URLField(verbose_name=_("Ссылка на видео"))
    main_image = models.ImageField(upload_to="tour/", verbose_name=_("Главное изображение"))
    personal_gear = models.ManyToManyField(to=Gear, verbose_name=_("Снаряжение"))
    includes = models.ManyToManyField(to=Includes, verbose_name=_("Включения"))
    excludes = models.ManyToManyField(to=Excludes, verbose_name=_("Исключения"))

    def __str__(self):
        return self.title

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


class Itinerary(models.Model):
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name=_('Тур'))
    date = models.DateField(verbose_name=_("Дата"), null=False)
    title = models.CharField(verbose_name=_("Заголовок"), max_length=255)
    meals = models.ForeignKey(Meal, on_delete=models.DO_NOTHING, verbose_name=_("Еда"))
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
        verbose_name_plural = 'Изображение комментариев'


class TourRating(models.Model):
    tour_id = models.ForeignKey(Tour, verbose_name=_("Тур"), on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(verbose_name=_("Рейтинг"),
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Пользователь"))

    def __str__(self):
        return f"{self.tour_id}, Пользователь: {self.user.name}, Рейтиинг: {self.rating}"

    class Meta:
        db_table = 'tour_rating'
        verbose_name = 'Рейтинг тура'
        verbose_name_plural = 'Рейтинги туров'


class Activity(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    destination = models.ForeignKey(Destination, related_name='activity', on_delete=models.CASCADE, verbose_name='Пункт')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'activity'
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'
