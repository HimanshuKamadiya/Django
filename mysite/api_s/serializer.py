from api_s.models import cookbook
from rest_framework import serializers
 
class cookbookserializers(serializers.Serializer):
    dish=serializers.CharField(max_length=20)
    detail=serializers.DictField()