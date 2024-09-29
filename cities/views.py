from django.shortcuts import render

from .models import City
# Create your views here.

__all__ = (
    'index',
)

def index(request, pk: int = None):

    if pk:
        ds = City.objects.filter(id=pk).first()
        context = {
            'ds': ds,
        }
        return render(request, 'detales.html', context)

    ds = City.objects.all()
    context = {
        'ds': ds
    }
    return render(request, 'index.html', context)
