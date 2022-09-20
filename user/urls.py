from django.urls import path

import user.views

urlpatterns = [
    path('profile/', user.views.UserProfileView.as_view(), name='user_profile'),
    path('users_list/', user.views.user_list, name='users_list'),
]