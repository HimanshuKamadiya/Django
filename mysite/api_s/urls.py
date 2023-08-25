from api_s.views import *
from django.urls import path,include


urlpatterns = [
    path('',api_views.as_view()),
    path('api_h/',api_h)
]
