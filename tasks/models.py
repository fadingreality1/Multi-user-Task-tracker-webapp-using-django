from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tasks(models.Model):
    status_choices = [
        ('c', 'completed'),
        ('p', 'pending'),
    ]
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=5, choices=status_choices, default='p')
    creation_date = models.DateField(default=timezone.now)
    due_date = models.DateField(auto_now_add=False, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    