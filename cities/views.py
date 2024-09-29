from django.shortcuts import render

from .models import City
# Create your views here.

__all__ = (
    'index',
)

def index(request):
    ds = City.objects.all()

    context = {
        'ds': ds
    }

    return render(request, 'index.html', context)
