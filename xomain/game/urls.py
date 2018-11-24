from django.urls import path
from .views import fp


urlpatterns = [
    path('', fp.as_view(), name='fp'),
]
