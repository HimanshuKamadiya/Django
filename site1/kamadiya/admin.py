from django.contrib import admin
from kamadiya.models import service
class s_ervices(admin.ModelAdmin):
    list_display = ('name', 'price')
    
admin.site.register(service,s_ervices)