from django.contrib import admin
from .models import cbv,contactform


class cb_v(admin.ModelAdmin):
    list_display=('f_model','s_model')
admin.site.register(cbv,cb_v)


class contact_f(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(contactform,contact_f)