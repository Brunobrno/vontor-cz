"""
ASGI config for vontor_cz project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vontor_cz.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

from home.routing import websocket_urlpatterns as home_ws_urls

ws_url_colection = [].append(home_ws_urls)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    ),
})

"""
ASGI se vyplatí používat až budeš využívat real-time komunikaci anebo websockety
"""
