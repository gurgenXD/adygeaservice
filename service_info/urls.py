from django.urls import path
from service_info.views import *


urlpatterns = [
    path('', ServiceInfoView.as_view(), name='service_info'),
    path('<structure_slug>/', StructureView.as_view(), name='structure'),
]