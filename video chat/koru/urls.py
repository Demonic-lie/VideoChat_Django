from django.urls import path
from . import views

app_name= 'koru'
urlpatterns = [
    path("", views.index, name="index"),
    path("host/", views.host, name="host"),
    path("users/", views.users, name="users"),
    path("call/", views.call, name="call"),
]