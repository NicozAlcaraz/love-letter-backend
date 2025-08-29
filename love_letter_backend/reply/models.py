from django.db import models

class Reply(models.Model):
    reply = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
