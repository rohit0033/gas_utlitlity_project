# filepath: /C:/Users/HP/Desktop/assignement/gas_utility_project/support/models.py
from django.db import models
from accounts.models import CustomUser  # Import your CustomUser model

class SupportRep(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add any additional fields specific to support reps here

    def __str__(self):
        return self.user.username