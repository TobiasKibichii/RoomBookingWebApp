from django.db import models

# Create your models here.

class Room(models.Model):
    ROOM_TYPES = [
        ('suite', 'Suite'),
        ('standard','Standard Room'),
        ('deluxe', 'Deluxe Room')
    ]
    
    CURRENCY_TYPES = [
        ('USD', 'USD'),
        ('EUR', 'EUR')
    ]
    
    name =models.CharField(max_length=100, blank=True, default='')
    type =models.CharField(max_length=100, choices=ROOM_TYPES)
    pricePerNight =models.IntegerField(default=150)
    currency =models.CharField(max_length=10, default='USD', choices=CURRENCY_TYPES)
    maxOccupancy =models.IntegerField(default=1)
    description =models.TextField(default=1000)
    
    def _str_(self):
        return f"{self.name} ({self.type})"


