from django.urls import path, include

import coffeeshop.views

urlpatterns = [
    path('/profile', coffeeshop.views.coffeeshop_card, name='coffeeshop'),
    # path('/coffeeshop/coffeeshop_list'),
    # path('/coffeeshop/drinks_menu', include('drink.urls'))
]