from django import forms
from feedback.models import *


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = ('phone',)
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': '+7 (___) ___-__-__',
                                            'id': 'CallBackModalPhone',
                                            'autofocus': 'autofocus'}),
        }


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name', 'email_or_phone', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Ваше имя',
                                           'autofocus': 'autofocus'}),
            'email_or_phone': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'E-mail или телефон',
                                                     'autofocus': 'autofocus'}),
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Ваше сообщение',
                                          'rows': 5,
                                          'autofocus': 'autofocus'}),
        }
