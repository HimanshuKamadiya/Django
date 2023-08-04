from django.db import models

class cbv(models.Model):
    f_model=models.CharField(max_length=100)
    s_model=models.CharField(max_length=100)
