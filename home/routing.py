from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path("ws/anonChat/", consumers.AnonymChatConsumer.as_asgi()),
]