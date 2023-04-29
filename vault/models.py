import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserSavedPassword(models.Model):
    class Meta:
        verbose_name_plural = 'User Passwords'
        
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user} | {self.title}'
