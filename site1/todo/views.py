from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, TemplateView,RedirectView,ListView,FormView
from .models import cbv


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
    template_name='template.html'
    context_object_name='key' #key for the dict
    paginate_by=2