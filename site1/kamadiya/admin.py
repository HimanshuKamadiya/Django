from django.contrib import admin
from kamadiya.models import service ,book ,blog,contact, free
class s_ervices(admin.ModelAdmin):
    list_display = ('name', 'price')
    
admin.site.register(service,s_ervices)

class bo_ok(admin.ModelAdmin):
    list_display=('content','page_no')
admin.site.register(book,bo_ok)

class blo_g(admin.ModelAdmin):
    list_display=( 'Blog_title','blog_content','author_name','date_of_publication')
admin.site.register(blog,blo_g)

class contactadmin(admin.ModelAdmin):
    list_display=('name','mobile','address','message')
admin.site.register(contact,contactadmin)

class fre_e(admin.ModelAdmin):
    list_display=('caption','img')

admin.site.register(free,fre_e)