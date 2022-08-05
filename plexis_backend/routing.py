from django.urls import re_path

from broadcast import consumers as broadcast_consumers
from lobby import consumers as lobby_consumers

websocket_urlpatterns = [
    re_path(r'ws/lobby/$', lobby_consumers.LobbyConsumer.as_asgi()),
    re_path(r'ws/featured/$', broadcast_consumers.FeaturedConsumer.as_asgi())
]
