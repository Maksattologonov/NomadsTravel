from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import TransportDistance

@receiver([post_save, post_delete], sender=TransportDistance)
def update_tour_day_total_distance(sender, instance, **kwargs):
    if not hasattr(instance, '_signal_processed'):
        instance._signal_processed = True
        instance.tour_day.update_total_distance()