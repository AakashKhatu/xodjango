from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import player_name
from game.models import game_data
from random import choices
import string
from time import sleep
from math import pow

n1 = 5
n2 = 10


class fp(TemplateView):
    template_name = 'game/fp.html'

    def get(self, request):
        form = player_name()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = player_name(request.POST)
        if form.is_valid():
            new_game = game_data()
            new_game.room_url = '/game/' + ''.join(choices(string.ascii_uppercase, k=n1))
            new_game.player1_id = ''.join(choices(string.ascii_uppercase, k=n2))
            new_game.player1_name = form.cleaned_data['your_name']
            new_game.turn = 1
            new_game.save()
            request.session['player_id'] = new_game.player1_id
            request.session['player_name'] = new_game.player1_name
            return render(request, 'game/thnx.html', {'text': new_game.player1_name, 'room_url': new_game.room_url})


class game_field_active(TemplateView):
    template_name = 'game_field/active.html'
    state = ['empty', 'x', 'o']

    def get(self, request, room_url):
        params = {'url': room_url}
        current_game = game_data.objects.get(room_url='/game/'+room_url)
        t = 1
        for i in [int(d) for d in str(current_game.board)]:
            params.update({str(t)+'_vis': self.state[i]})
            t += 1
        return render(request, self.template_name, params)

    def post(self, request, room_url):
        print(request.POST['board'])
        current_game = game_data.objects.get(room_url='/game/'+room_url)
        current_game.board = str(int(current_game.board) + current_game.turn*int(pow(10, int(request.POST['board']))))
        while len(current_game.board) is not 9:
            current_game.board = '0' + current_game.board
        current_game.save()
        render(request, 'game_field/test.html', {})
        return redirect('/game/'+room_url)


class game_field_passive(TemplateView):
    template_name = 'game_field/passive.html'

    def get(self, request, room_url):
        params = {'url': room_url}
        current_game = game_data.objects.get(room_url='/game/'+room_url)
        t = 1
        for i in [int(d) for d in str(current_game.board)]:
            params.update({str(t)+'_vis': self.state[i]})
            t += 1
        return render(request, self.template_name, params)
