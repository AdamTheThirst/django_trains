from django.contrib.auth import authenticate, login
from django.shortcuts import render

from accounts.forms import UserLoginForm


# Create your views here.

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'accounts/login.html', {'form': form})