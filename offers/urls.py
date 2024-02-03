# urls.py
from django.urls import path
from .views import HotelRoomOfferListCreate

urlpatterns = [
    path('', HotelRoomOfferListCreate.as_view(), name='hotel-room-offers'),
]
