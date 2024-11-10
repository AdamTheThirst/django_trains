from django.contrib.auth import logout
from django.urls import path

from accounts.views import login_view, logout_view
from cities.urls import app_name

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

