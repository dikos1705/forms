from django import forms 
from .models import *


class AddPostForm(forms.Form):
    mark = forms.CharField(max_length=255, label="Марка")
    model = forms.CharField(max_length=255,label= "Модель")
    description = forms.CharField(widget= forms.Textarea(attrs={'cols': 60, 'rows':10}))
    photo = forms.ImageField()
    price = forms.CharField(max_length=255 , )
    is_published = forms.BooleanField(initial=True)



