from django import forms
from event.models import Event
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
# from django.forms.widgets import 

class UserAuthForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class EventCreationForm(forms.Form):
    title = forms.CharField(max_length=1000)
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    date = forms.DateField(widget=forms.DateInput)
    description = forms.CharField(widget=forms.Textarea)

