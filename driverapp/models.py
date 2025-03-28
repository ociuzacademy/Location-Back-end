from django.db import models

# Create your models here.
from django.db import models

class DriverRegister(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    aadhar_card = models.ImageField(upload_to='aadhar_cards/')
    password = models.CharField(max_length=100)  # Storing plain text (Not secure)
    place = models.CharField(max_length=100)  # New field for the place
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.name} ({self.status})"

