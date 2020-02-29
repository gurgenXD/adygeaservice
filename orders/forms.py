from django import forms
from orders.models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email_or_phone')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Ваше имя',
                                           'autofocus': 'autofocus'}),
            'email_or_phone': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'E-mail или телефон',
                                                     'autofocus': 'autofocus'}),
        }
