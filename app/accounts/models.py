from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    # Address fields (UK-specific)
    address_line_1 = models.CharField("Address line 1", max_length=255, blank=True, null=True)
    address_line_2 = models.CharField("Address line 2", max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.email
