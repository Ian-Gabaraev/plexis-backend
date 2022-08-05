from celery import shared_task
from django.conf import settings
from django.core.cache import cache

from dictionary.models import Entry
from dictionary.serializers import EntrySerializer


@shared_task(name="cache_wod")
def cache_wod():
    """
    Cache the serialized representation of
    a random word
    :return: bool
    """
    entry = Entry.objects.order_by('?').first()
    entry_serialized = EntrySerializer(entry).data
    cache.set(settings.WOD_CACHE_KEY, entry_serialized, 87_000)

    return True
