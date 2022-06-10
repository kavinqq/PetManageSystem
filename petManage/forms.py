from django import forms


class TestForm(forms.Form):

    key = forms.IntegerField(label = "input a key", help_text = " ")
    value = forms.CharField(label = "input a value", help_text = "1")