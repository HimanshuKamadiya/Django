from rest_frame.views import *
from django.urls import path

urlpatterns = [
    path('',rest_api_views),
    path('rest/',rest_api_list_view.as_view()),
    path('bd/<int:pk>',rest_api_detail_view.as_view()),
]
