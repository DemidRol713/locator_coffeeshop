from django.urls import path, include

import coffeeshop.views

urlpatterns = [
    path('profile?<int:id>/', coffeeshop.views.coffeeshop_card, name='coffeeshop'),
    path('coffeeshop_list/', coffeeshop.views.CoffeeshopListView.as_view(), name='coffeeshop_list'),
    path('', coffeeshop.views.main_page, name='main_page')
    # path('/coffeeshop/drinks_menu', include('drink.urls'))
]