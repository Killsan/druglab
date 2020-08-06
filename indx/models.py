from django.db import models

class App_user(models.Model):
    nick = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.nick