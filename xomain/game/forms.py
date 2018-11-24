from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Enter your name", max_length=20)
