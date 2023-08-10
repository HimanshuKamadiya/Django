from django.contrib import admin
from.models import cookbook

# Register your models here.
class cookbookadmin(admin.ModelAdmin):
    list_display=['dish','detail']
admin.site.register(cookbook,cookbookadmin)
