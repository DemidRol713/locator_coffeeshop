from django import forms

from .models import SettingsCoffeeShop


class SettingCoffeeshopForm(forms.ModelForm):

    class Meta:
        model = SettingsCoffeeShop
        fields = '__all__'