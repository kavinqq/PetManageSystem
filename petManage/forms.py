from django import forms


class TestForm(forms.Form):

    key = forms.IntegerField()
    value = forms.CharField()