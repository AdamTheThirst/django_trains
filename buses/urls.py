from django.urls import path

from .views import *

app_name = 'buses'

urlpatterns = [
    # path('', buses_view, name='buses_index'),
    path('bus_list/', BusListView.as_view(), name='buses_index'),
    path('details/<int:pk>/', BusDetailView.as_view(), name='buses_detail'),
    path('badd_bus/', BusCreateView.as_view(), name='buses_create'),
    path('update/<int:pk>/', BusUpdateView.as_view(), name='buses_update'),
    path('delete/<int:pk>/', BusDeleteView.as_view(), name='buses_delete'),
]