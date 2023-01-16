from django import forms 
from .models import *


class AddTable(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
       