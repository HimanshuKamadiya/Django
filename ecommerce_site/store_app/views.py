from django.shortcuts import render

def e_store(request):
    context={}
    return render(request,'store.html',context)

def cart(request):
    context={}
    return render(request,'cart.html',context)

def checkout(request):
    context={}
    return render(request,'check_out.html',context)
