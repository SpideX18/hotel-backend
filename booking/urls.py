from django.urls import path
from .views import BookingListCreate

app_name = 'room'

urlpatterns = [
    path('', BookingListCreate.as_view(), name='bookings'),
]
