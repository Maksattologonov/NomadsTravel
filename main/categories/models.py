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


class VisaInformation(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    text = models.TextField(verbose_name=_("Описание"))
    created_at = models.DateField(default=timezone.now(), verbose_name=_("Дата создания"))

    def __str__(self):
        return self.text

    class Meta:
        db_table = "visa_information"
        verbose_name = "Информация о визе"
        verbose_name_plural = "Информации о визе"
