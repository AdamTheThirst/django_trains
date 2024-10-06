from django.shortcuts import render
from django.contrib import messages

from routes.forms import RouteForm


# Create your views here.

def home(request):
    form = RouteForm()
    context = {'form': form}
    return render(request, 'routes/display_list.html', context)

def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            ...
    else:
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        context = {'form': form}
        return render(request, 'routes/display_list.html', context)
