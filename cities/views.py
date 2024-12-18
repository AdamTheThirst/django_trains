from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .forms import CityForm
# from .forms import CityForm
from .models import City
# Create your views here.

__all__ = (
    'cities_view',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
    'CityListView',
)

def cities_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()


    form = CityForm()
    ds = City.objects.all()

    lst = Paginator(ds, 10)
    page_number = request.GET.get('page', 1)
    page_obj = lst.page(page_number)

    context = {
        # 'ds': ds,
        'page_obj': page_obj,
        'form': form,
        'page_obj': page_obj,
    }
    return render(request, 'display_list.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'detales.html'
    context_object_name = 'city'

class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'create.html'
    success_url = reverse_lazy('cities:cities_index')
    sucsess_message = f'Город успешно создан'

class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin ,UpdateView):
    model = City
    form_class = CityForm
    template_name = 'update.html'
    success_url = reverse_lazy('cities:cities_index')
    sucsess_message = f'Город успешно отредактирован'

class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'delete.html'
    success_url = reverse_lazy('cities:cities_index')
    sucsess_message = f'Город успешно удалён'
class CityListView(ListView):
    paginate_by = 5
    model = City
    template_name = 'display_list.html'

