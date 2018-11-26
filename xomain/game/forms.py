from django import forms


class player_name(forms.Form):
    your_name = forms.CharField(label="Enter your name", max_length=20)
