from django.db import models
from django.utils import timezone
# Create your models here.

def get_current_timestamp():
    return int(timezone.now().timestamp())
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.CharField(max_length=400)
    timeStamp = models.IntegerField(default=get_current_timestamp)
    def __str__(self):
        return f"{self.name}, timestamp: {self.timeStamp}"   