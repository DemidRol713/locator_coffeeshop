from django.urls import path, include

from coffeeshop import views

urlpatterns = [
    path('profile/<pk>', views.CoffeeShopView.as_view(), name='coffeeshop'),
    path('coffeeshop_list/', views.CoffeeshopListView.as_view(), name='coffeeshop_list'),
    # path('', views.main_page, name='main_page')
    # path('/coffeeshop/drinks_menu', include('drink.urls'))
]