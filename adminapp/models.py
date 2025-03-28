from django.db import models

# Create your models here.

class tbl_admin(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    pswd = models.CharField(max_length=100)

    def __str__(self):
        return self.email

from decimal import Decimal

class tbl_category(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to="category_products/")

    def __str__(self):
        return self.name


class Ward(models.Model):
    ward_number = models.IntegerField(unique=True)
    location = models.CharField(max_length=255)  # Stores "from-to" in one field

    def __str__(self):
        return f"Ward {self.ward_number}: {self.location}"


        
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)  # Unique Employee ID
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)  # Store hashed password in production
    image = models.ImageField(upload_to="employee_images/", null=True, blank=True)  # Optional image
    ward = models.ManyToManyField(Ward, related_name="employees")  # Changed to ManyToManyField

    def __str__(self):
        return f"{self.employee_id} - {self.name}"


from django.db import models

class WasteThreshold(models.Model):
    limit = models.FloatField(default=50)  # Default 50 kg
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Threshold: {self.limit} kg"



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
