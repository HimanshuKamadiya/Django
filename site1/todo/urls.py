from django.urls import path
from . import views
from todo.views import *

urlpatterns = [
    path('',todo_home.as_view()),
    path('temp/',temp_view.as_view(),name='temp'),
    path('list/',list_view.as_view(),name='list'),
    path('detail/<int:pk>/',detail_view.as_view(),name='detail')
]

