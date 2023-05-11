from rest_framework import serializers

from coffeeshop.models import CoffeeShop


class CoffeeShopSerializers(serializers.ModelSerializer):
    # name = serializers.CharField()
    # address = serializers.CharField(max_length=500)
    # description = serializers.CharField()
    # longitude = serializers.FloatField()
    # latitude = serializers.FloatField()
    # website = serializers.ListField(child=serializers.URLField())
    # opening_hours = serializers.CharField()
    # telephone = serializers.ListField(child=serializers.CharField(max_length=200))
    # email = serializers.ListField(child=serializers.EmailField())
    # social_networks = serializers.ListField(child=serializers.URLField())
    # images = serializers.ListField(child=serializers.ImageField())

    class Meta():
        model = CoffeeShop
        fields = '__all__'
        # fields = ('name', 'address', 'description', 'longitude', 'latitude', 'website', 'opening_hours', 'telephone',
        #           'email', 'social_networks', 'images')
