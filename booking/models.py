# myapp/models.py
from django.db import models

class Booking(models.Model):
    guestName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    checkIn = models.DateField()
    checkOut = models.DateField()
    specialRequests = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Assuming currency format
    numberOfRooms = models.IntegerField()

    def __str__(self):
        return f"{self.guestName} - {self.checkIn.strftime('%Y-%m-%d')} to {self.checkOut.strftime('%Y-%m-%d')}"
