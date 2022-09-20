from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from coffeeshop.models import CoffeeShop
from locator_coffeeshop import settings


# Create your views here.
def coffeeshop_card(request):
    pass


class CoffeeshopListView(ListView):
    template_name = "coffeeshop/coffeeshops.html"
    model = CoffeeShop
    queryset = CoffeeShop.manager.get_coffeeshop_list()

    def get_context_data(self, *, object_list=None, **kwargs):

        data = super().get_context_data(**kwargs)
        data['main_menu'] = settings.MAIN_MENU
        data['coffeeshop_list'] = self.model.manager.get_coffeeshop_list()

        return data


@login_required
def main_page(request):
    if request.user.is_authenticated:
        return redirect('user_profile')
    else:
        return redirect('login')