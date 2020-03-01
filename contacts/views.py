from django.shortcuts import render
from django.views import View
from contacts.models import *
from feedback.forms import FeedBackForm


class ContactsView(View):
    def get(self, request):
        addresses = Address.objects.all()
        phones = Phone.objects.all()
        emails = Email.objects.all()
        socials = Social.objects.all()
        schedule = Schedule.objects.all()
        map_code = MapCode.objects.first()

        feedback_form = FeedBackForm()

        context = {
            'addresses': addresses,
            'phones': phones,
            'emails': emails,
            'socials': socials,
            'schedule': schedule,
            'map_code': map_code,
            'feedback_form': feedback_form,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('contacts/contacts.html'), context)
