from django import forms

from cities.models import City


class CityForm(forms.ModelForm):
    city = forms.CharField(label='Добавить город',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Введите название города',
                           }))

    class Meta:
        model = City
        fields = ('city',)
