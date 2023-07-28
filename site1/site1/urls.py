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
from django.conf import settings
from django.conf.urls.static import static


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
    path('bookout/<slug>',views.book_out),
    path('blogout/',views.blog_a ),
    path('contactout/',views.con),
    path('upload/',views.media_pg),
    path('mediaout/',views.media_out),
    path('signup/',views.sigup,name='signup'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)