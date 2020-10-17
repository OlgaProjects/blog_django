from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Profile

class OurRegistration(UserCreationForm):
    email = forms.EmailField() # форма для почты

    class Meta: # доступные разрешения, связанное имя таблицы базы данных
        model = User
        fields = ['username', 'email', 'password1', 'password2']# отображение полей, в каком порядке

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileAvatar(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['avatar']



