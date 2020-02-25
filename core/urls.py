from django.urls import path
from core.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('content_pages/', ContentPagesView.as_view(), name='content_pages'),
]
