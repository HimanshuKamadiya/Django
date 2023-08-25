from rest_frame.models import rest_api_function
from rest_framework import serializers


class rest_apiserializer_s(serializers.Serializer):
    rest_model_1=serializers.CharField(max_length=100)
    rest_model_2=serializers.IntegerField() 
    
    
class rest_apiserializers(serializers.ModelSerializer):
     class Meta:
         model=rest_api_function
         fields=('id','rest_model_1','rest_model_2')
