from django.urls import path

from .views import *
from .views import CityDetailView

app_name = 'cities'

urlpatterns = [
    path('', cities_view, name='cities_index'),
    path('<int:pk>/', CityDetailView.as_view(), name='cities_detail'),

]