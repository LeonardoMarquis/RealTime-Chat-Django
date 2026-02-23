from django.urls import re_path    # vamos criar paths com expressoes regulares

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/S', ChatConsumer)
]



