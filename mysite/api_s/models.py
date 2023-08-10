from django.db import models

# Create your models here.
class cookbook(models.Model):
    dish=models.CharField(max_length=20)
    detail=models.TextField()
    