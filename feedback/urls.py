from django.urls import path
from feedback import views
from core.decorators import check_recaptcha


urlpatterns = [
    path('add_message/', check_recaptcha(views.FeedBackView.as_view()), name='feedback'),
    path('add_call/', views.CallBackView.as_view(), name='callback'),
]
