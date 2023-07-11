from django.http import HttpResponse
from django.shortcuts import render
from project2.models import dell


def sum(request):
    return HttpResponse('html')
def home(request):
    return render(request,'index.html')

def gabbar(request):
    a= dell.objects.all()
    b={'amit': a}
    return render(request,'dell.html',b)
    