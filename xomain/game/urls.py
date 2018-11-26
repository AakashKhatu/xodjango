from django.urls import path
from .views import fp, game_field_active, game_field_passive


urlpatterns = [
    path('', fp.as_view(), name='fp'),
    path('game/<str:room_url>/', game_field_active.as_view(), name='ng'),
    path('game/<str:room_url>/wait/', game_field_passive.as_view(), name='ng'),
]
