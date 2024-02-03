# serializers.py
from rest_framework import serializers
from .models import HotelRoomOffer

class HotelRoomOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomOffer
        fields = '__all__'
