from django.apps import AppConfig


class TourConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tour'
    verbose_name = 'Тур'
    verbose_name_plural = 'Туры'
