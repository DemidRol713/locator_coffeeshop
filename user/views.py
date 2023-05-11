from urllib import request

from cffi.backend_ctypes import unicode
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView
from requests import Session
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from user.forms import UserRegistrationForm, UserForm, ProfileChangeForm, ChangePasswordForm
from user.models import Profile
from user.serializers import UserRegistrationSerializers, UserLoginSerializers


def get_base_data(request):

    data = {
        'main_menu': settings.MAIN_MENU,
        'user_data': Profile.manager.get_user_by_id(request.user.id)
    }

    return data


class UserRegistrationView(CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/create_update_user.html'
    serializer_class = UserRegistrationSerializers
    model = Profile

    def get(self, request, *args, **kwargs):

        data = {'mode': 'create'}

        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(commit=False)
            except Exception as error:
                return Response({'error': error.args[0], 'mode': 'create'})
            # если мы находим пользователя в системе, то позволяем ему зайти в систему
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user is not None:
                login(self.request, user)
                return redirect('user_profile')
        else:
            # Присваиваем data ошибку
            data = serializer.errors
            data['mode'] = 'create'
            # Возвращаем ошибку
            return Response(data)


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    authentication_classes = (TokenAuthentication,)
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

    return redirect('login')


class LoginView(GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/login.html'
    serializer_class = UserLoginSerializers

    def get(self, request, *args, **kwargs):

        data = {'mode': 'create'}

        return Response(data)

    def post(self, request, *args, **kwargs):
        session = Session()

        user_data = {'username': self.request.data['username'], 'password': self.request.data['password']}

        data = session.post( 'jwt-create', user_data)
        if data.status_code == 200:
            return Response(data)
        # if user.is_active:
        #     return redirect('user_profile')
        # else:
        #     return render(self.request, 'user/login.html')


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