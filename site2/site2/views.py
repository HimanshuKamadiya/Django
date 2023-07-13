from django.http import HttpResponse
from django.shortcuts import render
from project2.models import dell,book


def sum(request):
    return HttpResponse('html')
def home(request):
    return render(request,'index.html')

def gabbar(request):
    a= dell.objects.all()
    b={'amit': a}
    return render(request,'dell.html',b)

def book_model(request):
    c=book.objects.all()
    data={
        'books':c
    }
    return render(request,'book.html',data)

def book_out(request,id):
    ab=book.objects.get(id=id)
    data={
        'name':ab
    }
    return render(request,'out.html',data)