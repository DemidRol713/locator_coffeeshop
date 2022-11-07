from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView
# from django.contrib.auth

from user.forms import UserRegistrationForm, UserForm, ProfileChangeForm, ChangePasswordForm
from user.models import Profile


def get_base_data(request):

    data = {
        'main_menu': settings.MAIN_MENU,
        'user_data': Profile.manager.get_user_by_id(request.user.id)
    }

    return data


class UserRegistrationView(CreateView):
    template_name = 'user/create_update_user.html'
    form_class = UserRegistrationForm
    model = Profile

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)
        data['mode'] = 'create'

        return data

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password1'])
        new_user.save()
        # если мы находим пользователя в системе, то позволяем ему зайти в систему
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        if user is not None:
            login(self.request, user)
            return redirect('user_profile')

    def form_invalid(self, form):
        data = {
            'user_data': form.cleaned_data,
            'mode': 'create',
            'error': form.errors
        }

        return render(self.request, 'user/create_update_user.html', data)


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    template_name = 'user/user_profile.html'
    model = Profile
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['app_name'] = 'Профиль'
        data.update(get_base_data(self.request))

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


@method_decorator(login_required, name='dispatch')
class ChangeProfileView(UpdateView):
    template_name = 'user/create_update_user.html'
    model = Profile
    form_class = ProfileChangeForm

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)
        data['app_name'] = 'Редактирование профиля'
        data['user_data'] = Profile.manager.get_user_by_id(self.request.user.id)
        data['mode'] = 'edit'

        return data

    def form_valid(self, form):

        form.save()

        return redirect('user_profile')

    def form_invalid(self, form):

        data = {
            'user_data': Profile.manager.get_user_by_id(self.request.user.id),
            'mode': 'edit',
            'error': form.errors
        }

        return render(self.request, 'user/create_update_user.html', data)


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(views.PasswordChangeView):
    template_name = 'user/create_update_user.html'
    form_class = ChangePasswordForm

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)
        data['app_name'] = 'Замена пароля'
        data['mode'] = 'change_password'

        return data

    def form_valid(self, form):
        form.save()

        return redirect('user_profile')

    def form_invalid(self, form):

        data = {
            "mode": 'change_password',
            'error': form.errors
        }

        return render(self.request, 'user/create_update_user.html', data)


def user_list(request):
    pass