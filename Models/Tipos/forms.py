from django import forms

from Models import Tipos


class armar(forms.ModelForm):
    class Meta:
        model = Tipos
        fields ='__all__'

