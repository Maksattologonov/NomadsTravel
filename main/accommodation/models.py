from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

from common.utils import get_elevation
from tour.managers import Location


class Accommodation(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Наименование"))
    price = models.PositiveIntegerField(verbose_name=_("Цена"))
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name=_("Локация"))
    elevation = models.FloatField(default=0, verbose_name=_("Высота над у.м."))
    main_image = models.ImageField(upload_to='accomodation', verbose_name=_("Главное изображение"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Размещение"
        verbose_name_plural = "Размещения"
        db_table = 'accommodation'

    def update_elevation(self):
        lat, lon =  self.location.lat, self.location.lon
        self.elevation = get_elevation(lat, lon)
        self.save(update_fields=['elevation'])


class AccommodationRating(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, verbose_name=_("Резмещение"))
    rating = models.DecimalField(verbose_name=_("Рейтинг"), max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return str(self.accommodation) + ": " + str(self.rating)

    class Meta:
        verbose_name = "Рейтинг места размещения"
        verbose_name_plural = "Рейтинги мест размещения"
        db_table = 'accommodation_rating'


class AccommodationImage(models.Model):
    accommodation_id = models.ForeignKey('Accommodation', on_delete=models.DO_NOTHING, verbose_name=_('Отель'))
    image = models.ImageField(upload_to='accommodations', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'accommodation_image'
        verbose_name = 'Изображение отеля'
        verbose_name_plural = 'Изображение отелей'


class Room(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, verbose_name=_("Тип"))
    size = models.PositiveSmallIntegerField(verbose_name=_("Размер"))
    mini_bar = models.BooleanField(default=False, verbose_name=_("Мини бар"))
    tv = models.BooleanField(default=False, verbose_name=_("Телевизор"))
    bed = models.CharField(max_length=255, verbose_name=_("Кровать"))
    bath = models.CharField(max_length=255, verbose_name=_("Ванная"))
    toilet = models.BooleanField(default=False, verbose_name=_("Туалет"))
    ac = models.BooleanField(default=False, verbose_name=_("Кондиционер"))
    window = models.CharField(max_length=255, verbose_name=_("Окно"))
    wifi = models.BooleanField(default=False, verbose_name=_("WIFI"))
    fridge = models.BooleanField(default=False, verbose_name=_("Холодильник"))

    def __str__(self):
        return str(self.accommodation.name) + ": " + str(self.type)

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"
        db_table = 'room'


class AccommodationIncludes(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    breakfast = models.BooleanField(default=False, verbose_name=_("Завтрак"))
    indoor_swimming_pool = models.BooleanField(default=False, verbose_name=_("Бассейн"))
    airport_shuttle = models.BooleanField(default=False, verbose_name=_("Трансфер до аэропорта"))
    non_smoking_rooms = models.BooleanField(default=False, verbose_name=_("Комната для некурящих"))
    fitness_center = models.BooleanField(default=False, verbose_name=_("Фитнесс"))
    free_wifi = models.BooleanField(default=False, verbose_name=_("Беслатный wifi"))
    room_service = models.BooleanField(default=False, verbose_name=_("Обслуживание номеров"))
    free_parking = models.BooleanField(default=False, verbose_name=_("Бесплатная парковка"))
    tea_maker_in_room = models.BooleanField(default=False, verbose_name=_("Чайник/кофеварка во всех номерах"))
    bar = models.BooleanField(default=False, verbose_name=_("Бар"))
    laundry = models.BooleanField(default=False, verbose_name=_("Прачечная"))

    def __str__(self):
        return str(self.accommodation.name)

    class Meta:
        db_table = "accommodation_includes"
        verbose_name = "Включение"
        verbose_name_plural = "Включения"
