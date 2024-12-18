from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from buses.models import Bus
from cities.models import City
from routes.forms import RouteForm, RouteModelForm
from routes.models import Route
from routes.utils import get_routes


# Create your views here.

def home(request):
    form = RouteForm()
    context = {'form': form}
    return render(request, 'routes/display_list.html', context)

def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/display_list.html', {form: form})
            return render(request, 'routes/display_list.html', context)

    else:
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        context = {'form': form}
        return render(request, 'routes/display_list.html', context)

def add_route(request):
    if request.method == 'POST':
        context = {}
        data = request.POST
        if data:
            print(data)
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            buses = data['buses'].split(',')

            buses_lst = [int(t) for t in buses if t.isdigit()]

            qs = Bus.objects.filter(id__in=buses_lst).select_related('from_city', 'to_city')

            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()

            form = RouteModelForm(
                initial={'from_city': cities[from_city_id],
                         'to_city': cities[to_city_id],
                         'route_travel_time': total_time,
                         'buses': qs,
                         }
            )
            context['form'] = form

        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'Нет данных для поиска')
        return redirect('/')

def save_route(request):
    if request.method == 'POST':
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Всё ок')
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'Some problems')
        return redirect('/')

class RouteListView(ListView):
    paginate_by = 5
    model = Route
    template_name = 'routes/list.html'

class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detales.html'
    context_object_name = 'route_detail'

class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    success_url = reverse_lazy('routes:list')
    template_name = 'routes/delete.html'

    def get(self, *args, **kwargs):
        messages.success(request, 'Route is removed')
        return self.post(request, *args, **kwargs)
