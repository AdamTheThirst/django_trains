from django.shortcuts import render

from routes.forms import RouteForm


# Create your views here.

def home(request):
    form = RouteForm()
    context = {'form': form}
    return render(request, 'routes/display_list.html', context)