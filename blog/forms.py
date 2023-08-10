from django import forms
from .models import Game, Player


class CreateGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('player_number', 'werwolf_number', 'include_amor', 'include_blinzel', 'include_seher', 'include_hexe',
                  'include_jaeger',)


class JoinGame_Key(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('game_key', )


class JoinGame_Name(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('player_name', )
