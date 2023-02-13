from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView
from django.core.paginator import Paginator
import folium

from coffeeshop.models import CoffeeShop
from settings_coffeeshop.forms import SettingCoffeeshopForm
from user.models import Profile
from settings_coffeeshop.models import SettingsCoffeeShop
from locator_coffeeshop import settings


def get_base_data(request):

    data = {
        'main_menu': settings.MAIN_MENU,
        'user_data': Profile.manager.get_user_by_id(request.user.id)
    }

    return data


@method_decorator(login_required, name='dispatch')
class CoffeeShopView(DetailView):
    template_name = "coffeeshop/coffeeshop_card.html"
    model = CoffeeShop

    def get_context_data(self, **kwargs):

        data = super(CoffeeShopView, self).get_context_data(**kwargs)
        data.update(get_base_data(self.request))
        data['coffeeshop'] = CoffeeShop.manager.get_coffeeshop_by_id(self.kwargs['pk'])
        data['coffeeshop'].opening_hours = data['coffeeshop'].opening_hours.split(';')
        data['app_name'] = data['coffeeshop'].name
        data['setting'] = SettingsCoffeeShop.manager.get_settings_by_id_coffeeshop(self.kwargs['pk'])
        if len(data['setting'] ) == 0:
            setting = SettingCoffeeshopForm({
                'id_coffeeshop': data['coffeeshop'].id,
                'type_content': 'main',
            })
            setting.save()
            data['setting'] = SettingsCoffeeShop.manager.get_settings_by_id_coffeeshop(self.kwargs['pk'])

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
    # paginator_class = Paginator(queryset, 10)
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):

        data = super().get_context_data(**kwargs)
        data.update(get_base_data(self.request))
        data['app_name'] = 'Список кофеен'
        data['main_menu'] = settings.MAIN_MENU
        coffeeshop_list = self.model.manager.get_coffeeshop_list()
        data['filters'] = settings.FILTERS_COFFEESHOP
        paginator = Paginator(coffeeshop_list, 10)
        page_number = self.request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        data['page_obj'] = paginator.get_page(page_number)

        map = folium.Map(location=[59.938732, 30.316229])
        for coffeeshop in coffeeshop_list:
            coordinates = [coffeeshop.latitude, coffeeshop.longitude]

            folium.Marker(
                location=coordinates,
                popup=folium.Popup('{name}<br>Адрес: {address}'.format(name=coffeeshop.name, address=coffeeshop.address),
                                   max_width=450)
            ).add_to(map)
        folium.LayerControl().add_to(map)
        map = map._repr_html_()
        data['map'] = map

        return data

    def post(self, request, *args, **kwargs):

        filter = self.request.POST
        tags_list = settings.FILTERS_COFFEESHOP
        tags = []
        for index_tag, tag in enumerate(tags_list):
            if filter.get(tag['name']) == 'on':
                tags.append(tag)
                tags_list[index_tag]['is_active'] = True

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

        map = folium.Map(location=[59.696, 30.681])
        for coffeeshop in coffeeshop_list_filtered:
            coordinates = [coffeeshop.latitude, coffeeshop.longitude]

            folium.Marker(
                location=coordinates,
                popup=folium.Popup('{name}<br>Адрес: {address}'.format(name=coffeeshop.name, address=coffeeshop.address), max_width=450),
            ).add_to(map)

        folium.LayerControl().add_to(map)

        map = map._repr_html_()

        data = {'filters': tags_list, 'coffeeshop_list': coffeeshop_list_filtered, 'map': map,
                'app_name': 'Список кофеен'}
        data.update(get_base_data(self.request))

        return render(self.request, "coffeeshop/coffeeshop_list.html", data)


@login_required
def main_page(request):

    # data = get_base_data(request)
    return redirect('coffeeshop_list')