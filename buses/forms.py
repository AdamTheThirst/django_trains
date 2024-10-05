from django import forms

from buses.models import Bus
from cities.models import City


class BusForm(forms.ModelForm):
    name = forms.CharField(label='Добавить маршрут',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Введите название маршрута',
                           }))

    from_city = forms.ModelChoiceField(label='Откуда ехать', queryset=City.objects.all(),
                           widget=forms.Select(attrs={
                               'class': 'form-control',
                           }))

    to_city = forms.ModelChoiceField(label='Куда ехать', queryset=City.objects.all(),
                           widget=forms.Select(attrs={
                               'class': 'form-control',
                           }))

    travel_time = forms.IntegerField(label='Время в пути',
                           widget=forms.NumberInput(attrs={
                               'class': 'form-control',
                               'placeholder': '12',
                           }))

    class Meta:
        model = Bus
        fields = ('name','from_city','to_city', 'travel_time')
