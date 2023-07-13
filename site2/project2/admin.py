from django.contrib import admin
from project2.models import dell,book
# Register your models here.
class delladmin(admin.ModelAdmin):
    list_display=('processor', 'card')
    
admin.site.register(dell,delladmin)

class bookadmin(admin.ModelAdmin):
    list_display=('book_name','author','description')
    
admin.site.register(book,bookadmin)
