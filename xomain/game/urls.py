from django.urls import path
from .views import fp, game_field, game_join


urlpatterns = [
    path('', fp.as_view(), name='fp'),
    path('game/<str:room_url>/', game_field.as_view(), name='ng'),
    path('game/<str:room_url>/join', game_join.as_view(), name='ng'),
]
