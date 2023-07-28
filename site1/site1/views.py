from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from .forms import uforms
from kamadiya.models import service,book,blog,contact,free
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    return  render(request, 'index.html')

def sum(request):
    return HttpResponse('html')

def dynamic_data(request):
    data={
        'name': ['django','web-dev','class'],
        }
    return render(request,'data.html',data)

def form(request):
    ans=0
    try:
        n=int(request.GET['num'])
        n1=int(request.GET['num1'])
        n2=request.GET['operator']
        if n2 =='+':
            ans=n+n1
        elif n2=='-':
            ans=n-n1
        elif n2=='/':
            ans=n%n1
        elif n2=='x':
            ans=n*n1
        else:
            ans='error'
    except:
        pass
    return render(request,'form.html',{'out':ans})

def form_1(request):
    c=0
    try:
        a=int(request.GET['num'])
        b=int(request.GET['num1'])
        c=a+b
        url='/out02/?output={}'.format(c)
        return HttpResponseRedirect(url)
    except:
        pass
    return render(request,'form1.html',{'out':c})

def out1(request):
    if request.method=="GET":
        out=request.GET.get('output') #variable
    return render(request,'output.html',{"out2":out})

def forms_py(request):
    a= uforms()
    data={'form':a}
    c=0
    try:
        if request.method=="POST":
            a=int(request.POST.get('int1'))
            b=int(request.POST.get('int2'))
            c=a+b
            data['out']=c
    except:
        pass
    return render(request,'form-py.html',data)

def calc(request):
    ans=''
    try:
        n1=int(request.GET['num'])
        n2=int(request.GET['num2'])
        
        if request.GET.get('add') =='' :
            ans= n1+n2
        elif request.GET.get('sub')=='' :
            ans=n1-n2
        elif request.GET.get('divide')=='' :
            ans= n1/n2
        else:
            ans=n1*n2
        print(ans)
    except:
        pass
    return render(request, 'calculator.html', {'re':ans})

def model_s(request):
    sa_data=service.objects.all()
    data={
        'service_data':sa_data,
    }
    return render(request, 'model.html', data)

def book_models(request):
    context=book.objects.all()
    a=Paginator(context,2)
    page_num=request.GET.get('page')
    f_varr=a.get_page(page_num)
    if request.method=='GET':
        a=request.GET.get('data')
        if a!=None:
            f_varr =book.objects.filter(name__icontains= a) #icontains gives suggestion of the element which contains a.
    
    data={
        'book_context': f_varr
    }
    
    return render(request,'book.html',data)

def book_out(request,slug):
    ba=book.objects.get(slug=slug)
    data={
        'name':ba
    }
    return render(request,'content.html',data)

def blog_a(request):
    blog_content=blog.objects.all()
    return render(request,'blog.html',{'blog_b':blog_content})


def con(request):
    if request.method=='POST':
        a=request.POST.get('name')
        b=request.POST.get('mobile')
        c=request.POST.get('address')
        d=request.POST.get('message')
        obj= contact(name=a,mobile=b,address=c,message=d)
        obj.save()
        
    return render(request,'contact.html')
def media_pg(request):
    if request.method=='POST':
        img_file=request.FILES.get('img',None)
        if img_file:
          a=request.POST.get('caption') 
          s=free(caption=a,img=img_file)
          s.save()
    return render (request,'media.html')
def media_out(request):
    b=free.objects.all()
    return render (request,'mediaout.html',{'ab':b})

def sigup(request):
    if request.method=='POST':
        name=request.POST['Name']
        username=request.POST['USER_NAME']
        email=request.POST['email']
        password=request.POST['Password']
        confirm_password=request.POST['Confirm_Password']
        
        
        myuser= User.objects.create_user(username,email,password)
        myuser.first_name=name
        myuser.save()
        return redirect('/')
    else:
        return HttpResponse('invalid')
    
def log_in(request):
    if request.method== 'POST':
        name=request.POST['name']
        password=request.POST['password']
        auth_out=authenticate(username=name,password=password)
        if auth_out is not None:
            login(request,auth_out)
            return redirect('/')
        else:
            messages.error('invalid login')
def log_out(request):
    logout(request)
    return redirect('/')