from django.contrib import admin
from .models import rest_api_function

# Register your models here.
class rest_api_admin(admin.ModelAdmin):
    list_display=['rest_model_1','rest_model_2']
admin.site.register(rest_api_function,rest_api_admin)