from django.contrib import admin
from kamadiya.models import service ,book
class s_ervices(admin.ModelAdmin):
    list_display = ('name', 'price')
    
admin.site.register(service,s_ervices)

class bo_ok(admin.ModelAdmin):
    list_display=('content','page_no')
admin.site.register(book,bo_ok)