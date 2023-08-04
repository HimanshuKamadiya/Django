from django.db import models

class cbv(models.Model):
    f_model=models.CharField(max_length=100)
    s_model=models.CharField(max_length=100)
    
    
class contactform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()