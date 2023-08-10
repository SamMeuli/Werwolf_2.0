from django.shortcuts import render, get_object_or_404, redirect
from .models import Role, Game, Player
from .forms import CreateGame, JoinGame_Key, JoinGame_Name

# Create your views here.


def main_page(request):

    return render(request, 'blog/main_page.html')


def new_game(request):
    if request.method == "POST":
        form = CreateGame(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            Game.game_host = request.user
            Player.player_key = request.user
            game.save()
            return redirect('lobby', pk=game.pk)
    else:
        form = CreateGame()
    return render(request, 'blog/new_game.html', {'form': form})


def join_game(request):
    games = Game.objects.order_by('game_key')
    return render(request, 'blog/join_game.html', {'games': games})


def lobby(request, pk):
    game_key = get_object_or_404(Game, pk=pk)
    return render(request, 'blog/lobby.html', {'lobby': game_key})
