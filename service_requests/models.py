from django.db import models
from django.conf import settings

class ServiceRequest(models.Model):
    CATEGORY_CHOICES = [
        ('Gas Leak', 'Gas Leak'),
        ('Billing Issue', 'Billing Issue'),
        ('Meter Installation', 'Meter Installation'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
