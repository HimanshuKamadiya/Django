from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_frame.models import rest_api_function
from rest_frame.serializer import rest_apiserializer_s,rest_apiserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def rest_api_views(request):
    data = rest_api_function.objects.all()
    serial = rest_apiserializer_s(data, many=True)
    json_data = JSONRenderer().render(serial.data)
    return HttpResponse(json_data, content_type='application/json')

class rest_api_list_view(APIView):
    def get(self, request, format=None):
        rest_api_book = rest_api_function.objects.all()
        serial = rest_apiserializers(rest_api_book, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    def post(self, request):
        serial = rest_apiserializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class rest_api_detail_view(APIView):
    def delete(self, request, pk, format=None):
        api_book = rest_api_function.objects.get(pk=pk)
        api_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk, format=None):
        api_book = rest_api_function.objects.get(pk=pk)
        serial = rest_apiserializers(api_book)
        return Response(serial.data)
    
    def put(self, request, pk, format=None):
        api_book = rest_api_function.objects.get(pk=pk)
        serial = rest_apiserializers(api_book, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

