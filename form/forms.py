from .models import data
from django import forms
from django.forms import ModelForm

class detail(ModelForm):
    class Meta:
        model = data
        fields=['name','email','address','phone','expertise','college']
