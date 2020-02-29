from django.urls import path
from orders import views
from core.decorators import check_recaptcha


urlpatterns = [
    path('add_order/', check_recaptcha(views.OrderView.as_view()), name='order'),
]
