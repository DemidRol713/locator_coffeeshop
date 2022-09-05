from django.urls import path
from django.contrib.auth import views

import user.views

urlpatterns = [
    path('profile?<int:id>', user.views.user_profile, name='profile'),
    path('users_list', user.views.user_list, name='users_list'),
    path('sign_in', views.LoginView.as_view(template_name='user/sign_in.html'), name='sign_in')
]