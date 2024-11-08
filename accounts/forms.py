from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.handlers.modwsgi import check_password

# импортирование встроенной модели юзера
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
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Username is incorrect')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Password is incorrect')

            user = authenticate(username=username, password=password)
