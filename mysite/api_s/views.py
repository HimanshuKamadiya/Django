from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,response
from api_s.models import*
from api_s.serializer import *
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
# Create your views here.

class api_views(View):
    def get(self,request):
        s=cookbookserializers()
        return JsonResponse(s.data)
   
def api_h(request):
    cook=cookbook.objects.all()
    serial=cookbookserializers(cook)
    jason_data=JSONRenderer().render(serial.data)
    return HttpResponse(jason_data,content_type='application/json')