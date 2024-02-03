from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', include('room.urls')),
    path('booking-details/', include('booking.urls')),
    path('offer-details/', include('offers.urls')),
]
