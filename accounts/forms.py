from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
    }))

    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')