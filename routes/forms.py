from django import forms

from buses.models import Bus
from cities.models import City


class RouteForm(forms.Form):

    route_from_city = forms.ModelChoiceField(label='Откуда ехать', queryset=City.objects.all(),
                           widget=forms.Select(attrs={
                               'class': 'form-control js-example-basic-single',
                           }))

    route_to_city = forms.ModelChoiceField(label='Куда ехать', queryset=City.objects.all(),
                           widget=forms.Select(attrs={
                               'class': 'form-control js-example-basic-single',
                           }))

    route_travel_time = forms.IntegerField(label='Время в пути',
                           widget=forms.NumberInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Время в пути',
                           }))

    cities = forms.ModelMultipleChoiceField(queryset=City.objects.all(),
                                            label='Через города',
                                            widget=forms.SelectMultiple(
                                                attrs={
                                                    'class': 'form-control js-example-basic-multiple',
                                                }
                                            ),
                                            required=False)


class RouteModelForm(forms.ModelForm):

    name = forms.CharField(label='Название маршрута',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Название маршрута',
                           }))

    from_city = forms.ModelChoiceField(label='Откуда ехать', queryset=City.objects.all(),
                           widget=forms.HiddenInput())

    to_city = forms.ModelChoiceField(label='Куда ехать', queryset=City.objects.all(),
                           widget=forms.HiddenInput())

    route_travel_time = forms.IntegerField(label='Время в пути',
                           widget=forms.HiddenInput())

    buses = forms.ModelMultipleChoiceField(queryset=Bus.objects.all(),
                                            label='Через города',
                                            widget=forms.SelectMultiple(
                                                attrs={
                                                    'class': 'form-control d-done',
                                                }
                                            ),
                                            required=False)
