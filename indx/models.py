from django.db import models
from django.conf import settings

class Bot(models.Model):
    name = models.CharField(max_length=20)
    token = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

