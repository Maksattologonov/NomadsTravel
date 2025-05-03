from django.apps import AppConfig


class AccommodationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accommodation'
    verbose_name = 'Размещение'
    verbose_name_plural = 'Размещения'

    def ready(self):
        import accommodation.signals
