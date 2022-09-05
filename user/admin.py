from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm, ProfileChangeForm
from .models import Profile


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ['username', 'first_name', 'last_name', 'email', 'date_of_birth',]

admin.site.register(Profile, CustomUserAdmin)