# views.py
from rest_framework import generics
from .models import HotelRoomOffer
from .serializers import HotelRoomOfferSerializer

class HotelRoomOfferListCreate(generics.ListCreateAPIView):
    queryset = HotelRoomOffer.objects.all()
    serializer_class = HotelRoomOfferSerializer
