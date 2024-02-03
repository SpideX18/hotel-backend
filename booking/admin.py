# myapp/admin.py
from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('guestName', 'email', 'checkIn', 'checkOut', 'price', 'numberOfRooms')

admin.site.register(Booking, BookingAdmin)
