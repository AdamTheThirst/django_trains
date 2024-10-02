from django.shortcuts import render
from django.views.generic import DetailView

from .forms import CityForm
# from .forms import CityForm
from .models import City
# Create your views here.

__all__ = (
    'cities_view',
)

def cities_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()


    form = CityForm()
    ds = City.objects.all()
    context = {
        'ds': ds,
        'form': form,
    }
    return render(request, 'cities.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'detales.html'
