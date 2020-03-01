from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from directions.models import *
from orders.forms import OrderForm
from contacts.models import Phone


class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.filter(is_active=True)

        context = {
            'teachers': teachers,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('directions/teachers.html'), context)


class DirectionsView(View):
    def get(self, request):
        directions = Direction.objects.filter(is_active=True)

        context = {
            'directions': directions,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('directions/directions.html'), context)


class DirectionView(View):
    def get(self, request, direction_slug):
        direction = get_object_or_404(Direction, slug=direction_slug, is_active=True)

        context = {
            'direction': direction,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('directions/direction.html'), context)


class CourseView(View):
    def get(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        order_form = OrderForm()
        call_phone = Phone.objects.first()

        context = {
            'course': course,
            'order_form': order_form,
            'call_phone': call_phone,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('directions/course.html'), context)


class SearchResultView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        courses = Course.objects.filter(title__icontains=query)

        context = {
            'courses': courses,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('directions/search-result.html'), context)


class CoursesJsonView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        products = Course.objects.filter(title__icontains=query)
        search_list = [item.title for item in products]

        return JsonResponse(search_list, safe=False)
