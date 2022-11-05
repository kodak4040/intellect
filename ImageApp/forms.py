from django import forms
from django.forms import ModelForm
from . models import  Book

class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields ='__all__'


class ConfirmForm(forms.Form):
    confirm = forms.BooleanField(label='confirm',required=True)        



