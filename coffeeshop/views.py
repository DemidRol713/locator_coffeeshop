from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
import folium

from coffeeshop.models import CoffeeShop
from coffeeshop.serializers import CoffeeShopSerializers
from user.models import Profile
from locator_coffeeshop import settings


def get_base_data(request):

    data = {
        'main_menu': settings.MAIN_MENU,
        'user_data': Profile.manager.get_user_by_id(request.user.id)
    }

    return data


@method_decorator(login_required, name='dispatch')
class CoffeeShopApiView(RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'coffeeshop/coffeeshop_card.html'
    # serializer_class = CoffeeShopSerializers
    # queryset = CoffeeShop.manager.all()

    def get(self, request, *args, **kwargs):
        data = {}
        data.update(get_base_data(self.request))
        coffeeshop = CoffeeShop.manager.get_coffeeshop_by_id(self.kwargs['pk'])
        coffeeshop.opening_hours = coffeeshop.opening_hours.split(';')
        app_name = coffeeshop.name

        coordinates = [coffeeshop.latitude, coffeeshop.longitude]
        map = folium.Map(location=coordinates, zoom_start=17)

        folium.Marker(
            location=coordinates,
            popup='{name}\nАдрес: {address}'.format(name=coffeeshop.name, address=coffeeshop.address)
        ).add_to(map)
        folium.LayerControl().add_to(map)

        map = map._repr_html_()

        return Response({'coffeeshop': coffeeshop, 'app_name': app_name, 'map': map,
                         'user_data': data['user_data'], 'main_menu': data['main_menu']})


@method_decorator(login_required, name='dispatch')
class CoffeeShopListAPIView(ListAPIView):
    template_name = "coffeeshop/coffeeshop_list.html"
    serializer_class = CoffeeShopSerializers
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        data = get_base_data(self.request)
        app_name = 'Список кофеен'
        coffeeshop_list = CoffeeShop.manager.get_coffeeshop_list()
        filters = settings.FILTERS_COFFEESHOP
        paginator = Paginator(coffeeshop_list, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        map = folium.Map(location=[59.938732, 30.316229])
        for coffeeshop in coffeeshop_list:
            coordinates = [coffeeshop.latitude, coffeeshop.longitude]

            folium.Marker(
                location=coordinates,
                popup=folium.Popup(
                    '{name}<br>Адрес: {address}'.format(name=coffeeshop.name, address=coffeeshop.address),
                    max_width=450)
            ).add_to(map)
        folium.LayerControl().add_to(map)
        map = map._repr_html_()

        return Response({'main_menu': data['main_menu'], 'user_data': data['user_data'], 'app_name': app_name,
                         'filters': filters, 'map': map, 'page_obj': page_obj, 'coffeeshop_list': coffeeshop_list})

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
                    if tag['name'] in coffeeshop.tags:
                        coffeeshop_list_filtered.append(coffeeshop)
                        break
                    pass
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

        data = get_base_data(self.request)

        return Response({'filters': tags_list, 'coffeeshop_list': coffeeshop_list_filtered, 'map': map,
                         'app_name': 'Список кофеен', 'main_menu': data['main_menu'],
                         'user_data': data['user_data']})


@login_required
def main_page(request):

    # data = get_base_data(request)
    return redirect('coffeeshop_list')