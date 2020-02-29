from django.urls import path
from works import views


urlpatterns = [
    path('', views.WorksView.as_view(), name='works'),
    path('<album_slug>/', views.AlbumView.as_view(), name='album'),
]
