from django import forms


class player_name(forms.Form):
    your_name = forms.CharField(label="Enter your name", max_length=20)


class xo_field(forms.Form):
    f = [[str(x), ''] for x in range(0, 9)]
    board = forms.ChoiceField(widget=forms.RadioSelect(), choices=f)
