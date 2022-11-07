from django import forms

from .models import SettingsCoffeeShop


class SettingCoffeeshopForm(forms.ModelForm):
    class Meta:
        model = SettingsCoffeeShop
        fields = ('id_coffeeshop', 'type_content')
