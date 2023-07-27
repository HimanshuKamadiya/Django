from django.http import HttpResponse
from django.shortcuts import render,redirect
from project2.models import dell,book
from django.contrib.auth.models import User


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

def signup(request):
    if request.method=='POST':
        name=request.POST['Name']
        username=request.POST['User_Name']
        email= request.POST['Email']
        password=request.POST['Password']
        confirm_password=request.POST['Confirm_Password']
        
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=name
        myuser.save()
        return redirect('/')
    else:
        return HttpResponse('invalid')