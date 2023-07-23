from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class service(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=500)

class book(models.Model):
    content=models.CharField(max_length=100)
    page_no=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='content', unique=True, null=True, default=None)

class blog(models.Model):
    Blog_title=models.CharField(max_length=100)
    blog_content=models.TextField(max_length=10000)
    author_name=models.CharField(max_length=100)
    date_of_publication=models.DateField()