from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

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
