from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView
import folium

from coffeeshop.models import CoffeeShop
from settings_coffeeshop.models import SettingsCoffeeShop
from file.models import File
from locator_coffeeshop import settings


@method_decorator(login_required, name='dispatch')
class CoffeeShopView(DetailView):
    template_name = "coffeeshop/coffeeshop_card.html"
    model = CoffeeShop

    def get_context_data(self, **kwargs):

        data = super(CoffeeShopView, self).get_context_data(**kwargs)
        data['coffeeshop'] = CoffeeShop.manager.get_coffeeshop_by_id(self.kwargs['pk'])
        data['setting'] = SettingsCoffeeShop.manager.get_settings_by_id_coffeeshop(self.kwargs['pk'])
        data['images'] = File.manager.get_files_by_id_setting(data['setting'].id)
        data['main_menu'] = settings.MAIN_MENU

        coordinates = [data['coffeeshop'].latitude, data['coffeeshop'].longitude]
        map = folium.Map(location=coordinates, zoom_start=17)

        folium.Marker(
            location=coordinates,
            popup='{name}\nАдрес: {address}'.format(name=data['coffeeshop'].name, address=data['coffeeshop'].address)
        ).add_to(map)
        folium.LayerControl().add_to(map)

        map = map._repr_html_()

        data['map'] = map

        return data


@method_decorator(login_required, name='dispatch')
class CoffeeshopListView(ListView):
    template_name = "coffeeshop/coffeeshop_list.html"
    model = CoffeeShop
    queryset = CoffeeShop.manager.get_coffeeshop_list()

    def get_context_data(self, *, object_list=None, **kwargs):

        data = super().get_context_data(**kwargs)
        data['main_menu'] = settings.MAIN_MENU
        data['coffeeshop_list'] = self.model.manager.get_coffeeshop_list()
        data['filters'] = settings.FILTERS_COFFEESHOP

        return data

    def post(self, request, *args, **kwargs):

        filter = self.request.POST
        tags_list = settings.FILTERS_COFFEESHOP
        tags = []
        for tag in tags_list:
            if filter.get(tag['name']) == 'on':
                tags.append(tag)

        coffeeshop_list = CoffeeShop.manager.get_coffeeshop_list()
        coffeeshop_list_filtered = []
        if tags:
            for coffeeshop in coffeeshop_list:
                for tag in tags:
                    settings_coffeeshop = SettingsCoffeeShop.manager.get_settings_by_id_coffeeshop(coffeeshop.id)
                    if tag['name'] in settings_coffeeshop.tags:
                        coffeeshop_list_filtered.append(coffeeshop)
                        break
        else:
            coffeeshop_list_filtered = coffeeshop_list

        data = {'main_menu': settings.MAIN_MENU, 'filters': settings.FILTERS_COFFEESHOP,
                'coffeeshop_list': coffeeshop_list_filtered}

        return render(self.request, "coffeeshop/coffeeshop_list.html", data)

@login_required
def main_page(request):
    if request.user.is_authenticated:
        return redirect('user_profile')
    else:
        return redirect('login')