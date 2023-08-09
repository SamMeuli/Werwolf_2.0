from django.db import models
from django.conf import settings

# Create your models here.


class Role(models.Model):
    role_title = models.CharField(max_length=50)
    description = models.TextField()
    is_evil = models.BooleanField()

    def __str__(self):
        return self.role_title


class Game(models.Model):
    game_host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    game_key = models.PositiveIntegerField(default=1)
    player_number = models.PositiveIntegerField(default=8)
    werwolf_number = models.PositiveIntegerField(default=2)
    include_amor = models.BooleanField(default=False)
    include_blinzel = models.BooleanField(default=False)
    include_seher = models.BooleanField(default=False)
    include_hexe = models.BooleanField(default=False)

    def __str__(self):
        return self.game_key

    def publish(self):
        self.safe()



class Player(models.Model):
    player_name = models.CharField(max_length=20, default="Guest")
    roletype = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_alive = models.BooleanField()
    joined_games = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_key = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
