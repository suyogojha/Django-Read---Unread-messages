from turtle import color
from django.contrib import admin
from .models import *
from django.utils.html import format_html



# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'sub', 'situation']
    list_display = ['name', 'email', 'sub', 'status', '_']
    list_per_page = 5
    
    def _(self, obj):
        if obj.situation == 'Read':
            return True
        else:
            return False
        
    _.boolean = True
    
    
    def status(self, obj):
        if obj.situation == 'Read':
            color = '#FEFE22'
        else:
            color = '#c92a2a'
        return format_html('<strong><p style="color: {};">{}</p></strong>'.format(color, obj.situation))
    status.allow_tags = True
            