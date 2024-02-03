# models.py
from django.db import models

class HotelRoomOffer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField()

    def __str__(self):
        return self.name
