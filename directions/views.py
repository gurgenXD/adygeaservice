from django.shortcuts import render, get_object_or_404
from django.views import View
from directions.models import *
from orders.forms import OrderForm


class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.filter(is_active=True)

        context = {
            'teachers': teachers,
        }
        return render(request, 'directions/teachers.html', context)


class DirectionsView(View):
    def get(self, request):
        directions = Direction.objects.filter(is_active=True)

        context = {
            'directions': directions,
        }
        return render(request, 'directions/directions.html', context)


class DirectionView(View):
    def get(self, request, direction_slug):
        direction = get_object_or_404(Direction, slug=direction_slug, is_active=True)

        context = {
            'direction': direction,
        }
        return render(request, 'directions/direction.html', context)


class CourseView(View):
    def get(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        order_form = OrderForm()

        context = {
            'course': course,
            'order_form': order_form,
        }
        return render(request, 'directions/course.html', context)
