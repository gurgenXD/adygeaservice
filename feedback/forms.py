from django import forms
from feedback.models import *


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name', 'email_or_phone', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Ваше имя'}),
            'email_or_phone': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'E-mail или телефон'}),
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Ваше сообщение',
                                          'rows': 4}),
        }
