from django.db import models

class dell(models.Model):
    processor=models.CharField(max_length=100)
    card=models.CharField(max_length=200)

class book (models.Model):
    book_name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    