"""
URL configuration for site1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('abc/', views.sum),
    path('',views.home),
    path('data/',views.dynamic_data),
    path('form/',views.form),
    path('out/',views.form_1),
    path('out02/',views.out1),
    path('out03/',views.forms_py),
    path('calc/',views.calc),
    path('models/',views.model_s),
    path('bookmodel/',views.book_models),
    path('bookout/<id>',views.book_out),
]
