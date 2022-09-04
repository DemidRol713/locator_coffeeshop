from django.urls import path, include

import coffeeshop.views

urlpatterns = [
    path('coffeeshop/profile', coffeeshop.views.coffeeshop_card),
    # path('/coffeeshop/coffeeshop_list'),
    # path('/coffeeshop/drinks_menu', include('drink.urls'))
]