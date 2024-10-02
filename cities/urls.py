from django.urls import path

from .views import *
from .views import CityDetailView, CityCreateView, CityUpdateView

app_name = 'cities'

urlpatterns = [
    path('', cities_view, name='cities_index'),
    path('details/<int:pk>/', CityDetailView.as_view(), name='cities_detail'),
    path('add_city/', CityCreateView.as_view(), name='cities_create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='cities_update'),
]