# models.py
from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set default user ID as an example
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    date = models.DateField('Date')
    content = models.TextField(default='')
    location = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title
