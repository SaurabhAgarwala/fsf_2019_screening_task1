from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assignee = models.ManyToManyField(User)
    created_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title