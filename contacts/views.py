from django.shortcuts import render
from django.views import View
from contacts.models import *
from feedback.forms import FeedBackForm


class ContactsView(View):
    def get(self, request):
        addresses = Address.objects.all()
        phones = Phone.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()

        feedback_form = FeedBackForm()

        context = {
            'addresses': addresses,
            'phones': phones,
            'emails': emails,
            'map_code': map_code,
            'feedback_form': feedback_form,
        }
        
        return render(request, 'contacts/contacts.html', context)
