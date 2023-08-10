from django.shortcuts import render
from django.http import JsonResponse
from api_s.models import*
from api_s.serializer import *
from django.views.generic import View
from rest_framework.views import APIView
# Create your views here.

class api_views(View):
    def get(self,request):
        s=cookbookserializers()
        return JsonResponse(s.data)