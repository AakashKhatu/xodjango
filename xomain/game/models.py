from django.db import models


class game_field(models.Model):
    field = models.BooleanField()
    player1 = models.TextField()
    player2 = models.TextField()
