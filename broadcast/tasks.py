from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.conf import settings

from dictionary.models import Entry
from dictionary.serializers import EntrySerializer


@shared_task(name="suggest_a_word")
def suggest_a_word():
    broadcast_room_name = settings.BROADCAST_ROOMS['FEATURED']
    word = Entry.objects.order_by('?').first()
    serialized = EntrySerializer(word).data

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(broadcast_room_name, {
        "message": serialized,
        "type": "chat_message"
    })

    return
