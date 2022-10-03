from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class ProfileChangeForm(UserChangeForm):
    """

    """
    class Meta(UserChangeForm):
        model = Profile
        fields = ("username", 'first_name', 'last_name', 'email', 'date_of_birth')

    def clean_email(self):
        cleaned_data = super().clean()
        if Profile.manager.filter(email=cleaned_data.get('email')).exists():
            self.fields.add_error('email', "Эта почта уже зарегистрирована")
        return cleaned_data.get('email')

    def clean_username(self):
        cleaned_data = super().clean()
        if Profile.objects.filter(email=cleaned_data.get('username')).exists():
            self.fields.add_error('username', "Этот логин уже зарегистрирован")
        return cleaned_data.get('username')


class UserRegistrationForm(UserCreationForm):
    """

    """
    password1 = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', max_length=20, widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1')

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Ошибка! Пароли не совпадают!')
        return cd['password2']

    def clean_email(self):
        cleaned_data = super().clean()
        if Profile.manager.filter(email=cleaned_data.get('email')).exists():
            self.fields.add_error('email', "Эта почта уже зарегистрирована")
        return cleaned_data.get('email')

    def clean_username(self):
        cleaned_data = super().clean()
        if Profile.objects.filter(email=cleaned_data.get('username')).exists():
            self.fields.add_error('username', "Этот логин уже зарегистрирован")
        return cleaned_data.get('username')


class UserLoginForm(forms.Form):
    """

    """
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('username', 'password')


class UserForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'first_name', "last_name", "email", 'date_of_birth']
