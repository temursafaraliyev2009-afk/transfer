from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),


    path(
        'player/<int:pk>/',
        views.player_detail,
        name='detail'
    ),


    path(
        'player/create/',
        views.player_create,
        name='create'
    ),

    path(
        'player/<int:pk>/update/',
        views.player_update,
        name='update'
    ),

    path(
        'player/<int:pk>/delete/',
        views.player_delete,
        name='delete'
    ),

]