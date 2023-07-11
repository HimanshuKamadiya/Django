from django.db import models

class dell(models.Model):
    processor=models.CharField(max_length=100)
    card=models.CharField(max_length=200)
    