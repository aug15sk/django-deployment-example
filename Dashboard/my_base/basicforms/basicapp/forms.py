from django import forms
from django.core import validators

def check_for_x(value):
    if value[0].lower() != 'x':
        raise forms.ValidationError("Name needs to start with x")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_x])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput)
