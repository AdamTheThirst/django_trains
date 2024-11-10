from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView


from .forms import BusForm
from .models import Bus
# Create your views here.

__all__ = (
    'buses_view',
    'BusDetailView',
    'BusCreateView',
    'BusUpdateView',
    'BusDeleteView',
    'BusListView',
)

def buses_view(request):

    form = BusForm()
    ds = Bus.objects.all()

    lst = Paginator(ds, 10)
    page_number = request.GET.get('page', 1)
    page_obj = lst.page(page_number)

    context = {
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'buses/display_list.html', context)

class BusDetailView(DetailView):
    queryset = Bus.objects.all()
    template_name = 'buses/detales.html'
    context_object_name = 'Bus'

class BusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Bus
    form_class = BusForm
    template_name = 'buses/create.html'
    success_url = reverse_lazy('buses:buses_index')
    sucsess_message = f'Автобусный маршрут успешно создан'

class BusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Bus
    form_class = BusForm
    template_name = 'buses/update.html'
    success_url = reverse_lazy('buses:buses_index')
    sucsess_message = f'Автобусный маршрут успешно отредактирован'

class BusDeleteView(LoginRequiredMixin, DeleteView):
    model = Bus
    template_name = 'buses/delete.html'
    success_url = reverse_lazy('buses:buses_index')
    sucsess_message = f'Автобусный маршрут успешно удалён'

class BusListView(ListView):
    paginate_by = 5
    model = Bus
    template_name = 'buses/display_list.html'

