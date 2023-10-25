from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    type_of = models.CharField(max_length=255, verbose_name=_("Тип места"), help_text="Кемпинг, Город, Лагерь")

    def __str__(self):
        return self.type_of

    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Visa(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    text = models.TextField(verbose_name=_("Описание"))
    created_at = models.DateField(default=timezone.now, verbose_name=_("Дата создания"))

    def __str__(self):
        return self.title

    class Meta:
        db_table = "visa_information"
        verbose_name = "Информация о визе"
        verbose_name_plural = "Информации о визе"


class Health(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    text = models.TextField(verbose_name=_("Описание"))
    created_at = models.DateField(default=timezone.now, verbose_name=_("Дата создания"))

    def __str__(self):
        return self.title

    class Meta:
        db_table = "health_information"
        verbose_name = "Информация о здоровье"
        verbose_name_plural = "Информации о здоровье"


class Gear(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Снаряжение"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "gear"
        verbose_name = "Снаряжение"
        verbose_name_plural = "Снаряжении"


class Includes(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "includes"
        verbose_name = "Включение"
        verbose_name_plural = "Включения"


class Excludes(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "excludes"
        verbose_name = "Исключение"
        verbose_name_plural = "Исключения"


class Meal(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "meal"
        verbose_name = "Еда"
        verbose_name_plural = "Еды"


class Entertainment(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Развлечения"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "entertainment"
        verbose_name = "Развлечение"
        verbose_name_plural = "Развлечения"
