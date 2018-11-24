from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import NameForm


class fp(TemplateView):
    template_name = 'game/fp.html'
    def get(self, request):
        form = NameForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['your_name']
            return render(request, 'game/thnx.html', {'text': text})
