from django.db import models

class Letters(models.Model):
    reply = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
