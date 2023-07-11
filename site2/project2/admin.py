from django.contrib import admin
from project2.models import dell
# Register your models here.
class delladmin(admin.ModelAdmin):
    list_display=('processor', 'card')
    
admin.site.register(dell,delladmin)

