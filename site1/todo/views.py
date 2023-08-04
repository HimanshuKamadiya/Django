from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, TemplateView,RedirectView,ListView,FormView
from .models import cbv,contactform
from todo.forms import *
from django.urls import reverse_lazy


class todo_home(View):
    def get(self,request):
        return HttpResponse(' Hello this is cbv')
    def post(self,request):
        pass

class temp_view(TemplateView):
    template_name ='template.html'    # active var
    
class redirect_temp(RedirectView):
    url='/todo/temp/' #url=

class list_view(ListView):
    model=cbv # active var
    template_name='list.html'
    context_object_name='key' #key for the dict
    paginate_by=2
    
class detail_view(DetailView):
    model=cbv
    template_name='details.html'
    context_object_name='name'
    
class form_view(FormView):
    template_name= 'todo_forms.html'
    form_class=contactform_
    success_url= reverse_lazy('form')
    
    def form_valid(self, form):
        name=form.cleaned_data['name']
        message=form.cleaned_data['message']
        email=form.cleaned_data['email']
        a=contactform.objects.create(name=name,email=email,message=message)
        a.save()
        return super().form_valid(form)