from django.shortcuts import render

from .models import City
# Create your views here.

__all__ = (
    'cities_view',
)

def cities_view(request, pk: int = None):

    if pk:
        ds = City.objects.filter(id=pk).first()

        if ds is None:
            ds = City.objects.first()

        context = {
            'ds': ds,
        }
        return render(request, 'detales.html', context)

    ds = City.objects.all()
    context = {
        'ds': ds
    }
    return render(request, 'cities.html', context)
