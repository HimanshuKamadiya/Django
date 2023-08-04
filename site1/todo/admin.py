from django.contrib import admin
from .models import cbv

class cb_v(admin.ModelAdmin):
    list_display=('f_model','s_model')
admin.site.register(cbv,cb_v)