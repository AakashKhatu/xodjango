from django.db import models
# from django.contrib.auth.models import User


class game_data(models.Model):
    board = models.IntegerField(default=000000000)
    turn = models.IntegerField(default=0)
    room_url = models.CharField(max_length=5, default='room_url')
    player1 = models.CharField(max_length=20, default='player1_id')
    player1_name = models.CharField(max_length=20, default='player1_name')
    player2 = models.CharField(max_length=20, default='player2_id')
    player2_name = models.CharField(max_length=20, default='player2_name')
