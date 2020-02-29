from django.urls import path
from directions import views


urlpatterns = [
    path('', views.DirectionsView.as_view(), name='directions'),
    path('teachers/', views.TeachersView.as_view(), name='teachers'),
    path('courses/<course_slug>/', views.CourseView.as_view(), name='course'),
    path('<direction_slug>/', views.DirectionView.as_view(), name='direction'),
]
