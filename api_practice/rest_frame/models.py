from django.db import models

class rest_api_function(models.Model):
    rest_model_1=models.CharField(max_length=100)
    rest_model_2=models.TextField()
    
    def __str__(self):
      return self.rest_model_1
