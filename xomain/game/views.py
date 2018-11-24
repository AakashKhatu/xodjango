from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import player_name, xo_field
from game.models import game_data
from random import choices
import string

N = 5


class fp(TemplateView):
    template_name = 'game/fp.html'

    def get(self, request):
        form = player_name()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = player_name(request.POST)
        if form.is_valid():
            new_game = game_data()
            new_game.room_url = '/game/' + ''.join(choices(string.ascii_uppercase, k=N))
            new_game.player1_name = form.cleaned_data['your_name']
            new_game.save()
            return render(request, 'game/thnx.html', {'text': new_game.player1_name, 'room_url': new_game.room_url})


class game_field(TemplateView):
    template_name = 'game_field/gf.html'

    def get(self, request, room_url):
        form = xo_field()
        return render(request, self.template_name, {'url': room_url, 'xo_field': form})
