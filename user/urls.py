from django.urls import path

from user import views
urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('users_list/', views.user_list, name='users_list'),
    path('edit_profile/<int:pk>', views.EditProfileView.as_view(), name='edit_profile')
]