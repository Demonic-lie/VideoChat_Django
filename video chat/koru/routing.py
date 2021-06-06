from django.urls import path
from .consumers import WSConsumers

ws_urlpatterns = [
    path('ws/some_url/', WSConsumers.as_asgi())
]