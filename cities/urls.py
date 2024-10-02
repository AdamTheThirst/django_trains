from django.urls import path

from .views import *

app_name = 'cities'

urlpatterns = [
    # path('', cities_view, name='cities_index'),
    path('', CityListView.as_view(), name='cities_index'),
    path('details/<int:pk>/', CityDetailView.as_view(), name='cities_detail'),
    path('add_city/', CityCreateView.as_view(), name='cities_create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='cities_update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='cities_delete'),
]