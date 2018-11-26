from django.db import models
# from django.contrib.auth.models import User


class game_data(models.Model):
    board = models.CharField(max_length=9, default='000000000')
    turn = models.IntegerField(default=0)
    room_url = models.CharField(max_length=11, default='url')
    player1_id = models.CharField(max_length=20, default='player1_id')
    player1_name = models.CharField(max_length=20, default='player1_name')
    player2_id = models.CharField(max_length=20, default='player2_id')
    player2_name = models.CharField(max_length=20, default='player2_name')
