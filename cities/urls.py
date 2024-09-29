from django.urls import path

from .views import *

app_name = 'cities'

urlpatterns = [
    path('', index, name='cities_index'),
    path('<int:pk>/', index, name='cities_detail'),
]