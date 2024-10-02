from django import forms

from cities.models import City


class CityForm(forms.ModelForm):
    city = forms.CharField(label='Добавить город')

    class Meta:
        model = City
        fields = ('city',)
