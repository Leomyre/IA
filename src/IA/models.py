# ai/models.py
from django.db import models

class APIKey(models.Model):
    name = models.CharField(max_length=100, unique=True)
    key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
