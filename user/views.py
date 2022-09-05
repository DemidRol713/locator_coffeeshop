from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from user.forms import UserRegistrationForm


# Create your views here.
def registration(request):
    if request.method == "POST":
        user_data = request.POST
        user_form = UserRegistrationForm(user_data)
        if user_form.is_valid():
            # если пользователь ввел правильные данные, то сохраняем его в базе данных
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            # если мы находим пользователя в системе, то позволяем ему зайти в систему
            user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('profile?')

    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/registration.html', {'user_form': user_form})


def sign_in(request):
    pass


def user_profile(request, id):
    if request.method == "GET":
        return render(request, 'user/user_profile.html')


def user_list(request):
    pass