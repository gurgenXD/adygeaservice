from django.views import View
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from orders.forms import *
from core.models import MailToString
from directions.models import Course


class OrderView(View):
    def post(self, request):
        order_form = OrderForm(request.POST)
        status = 0

        if order_form.is_valid() and request.recaptcha_is_valid:
            current_site = get_current_site(request)
            mail_subject = 'Новый заказ на сайте: ' + current_site.domain
            course_id = int(request.POST.get('course_id'))
            course = Course.objects.get(id=course_id)
            order = order_form.save(commit=False)
            order.course = course
            order.save()
            message = render_to_string('orders/order_message.html', {
                'domain': current_site.domain,
                'email_or_phone': order.email_or_phone,
                'name': order.name,
                'direction': course.direction.title,
                'course': course.title,
            })
            to_email = MailToString.objects.first().email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            status = 1

        context = {
            'status': status,
        }
        return JsonResponse(context)
