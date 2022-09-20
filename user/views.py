from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView
# from django.contrib.auth

from user.forms import UserRegistrationForm, UserForm
from user.models import Profile


class UserRegistrationView(CreateView):
    template_name = 'user/registration.html'
    form_class = UserRegistrationForm
    model = Profile

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password1'])
        new_user.save()
        # если мы находим пользователя в системе, то позволяем ему зайти в систему
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        if user is not None:
            login(self.request, user)
            return redirect('user_profile')


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    template_name = 'user/user_profile.html'
    model = Profile
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        user = Profile
        data = super().get_context_data(**kwargs)
        data['user_data'] = user.manager.get_user_by_id(self.request.user.id)
        data['mode'] = 'view'
        data['main_menu'] = settings.MAIN_MENU
        x = data['user_data']

        return data


def logout_view(request):
    logout(request)
    return redirect('login')


class LoginView(views.LoginView):
    template_name = 'user/login.html'

    def form_valid(self, form):
        user_data = form.cleaned_data
        user = authenticate(username=user_data['username'], password=user_data['password'])
        if user.is_active:
            login(self.request, user)
            return redirect('user_profile')
        else:
            return render(self.request, 'user/login.html')


def user_list(request):
    pass