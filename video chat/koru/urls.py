from django.urls import path
from . import views

app_name= 'koru'
urlpatterns = [
    path("", views.index, name="index"),
    path("host/", views.host, name="host"),
    path("hostcall/", views.hostcall, name="hostcall"),
    path("users/", views.users, name="users"),
    #path('<str:room_name>/', views.call, name='call'),
]