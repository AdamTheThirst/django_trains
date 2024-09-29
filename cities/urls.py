from django.urls import path

from .views import *

app_name = 'cities'

urlpatterns = [
    path('', cities_view, name='cities_index'),
    path('<int:pk>/', cities_view, name='cities_detail'),
]