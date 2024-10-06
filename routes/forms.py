from django import forms

from cities.models import City


class RouteForm(forms.Form):

    route_from_city = forms.ModelChoiceField(label='Откуда ехать', queryset=City.objects.all(),
                           widget=forms.Select(attrs={
                               'class': 'form-control',
                           }))

    route_to_city = forms.ModelChoiceField(label='Куда ехать', queryset=City.objects.all(),
                           widget=forms.Select(attrs={
                               'class': 'form-control',
                           }))

    route_travel_time = forms.IntegerField(label='Время в пути',
                           widget=forms.NumberInput(attrs={
                               'class': 'form-control',
                               'placeholder': '12',
                           }))

    cities = forms.ModelMultipleChoiceField(queryset=City.objects.all(),
                                            label='Через города',
                                            widget=forms.CheckboxSelectMultiple(
                                                attrs={
                                                    'class': 'form-control',
                                                    'placeholder': 'Какие города хотите посетить?',
                                                }
                                            ),
                                            required=False)