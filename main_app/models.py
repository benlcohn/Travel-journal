from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Journal(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=350)
  date = models.DateField('Date')
