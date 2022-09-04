from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class ProfileCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileChangeForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ('username', 'email')


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Repeat password', max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            raise forms.ValidationError('Ошибка! Пароли не совпадают!')
        return cd['password_2']