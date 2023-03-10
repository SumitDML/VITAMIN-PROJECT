from rest_framework import serializers
from .models import *


class SunshineAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SunshineAvailability
        fields = "__all__"
        # fields = ['id', 'Month', 'Strength',]


# class ZoneSerializer(serializers.ModelSerializer):
#     strengths = SunshineAvailabilitySerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Zones
#         fields = ['ZoneID', 'LatitudeMin', 'LatitudeMax', 'NorthSouth', 'strengths']


class ZoneViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zones
        fields = ['id', 'LatitudeMin', 'LatitudeMax', 'NorthSouth']


class ZipCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipCodes
        fields = "__all__"


class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabs
        fields = ['tab_id', 'name', 'display_name']


class TabChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabChild
        fields = ['tab_child_id', 'display_name']


class TabChildNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabChild
        fields = ['name']


def getGenericSerializer(model_arg):
    class GenericSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_arg
            fields = '__all__'

    return GenericSerializer
