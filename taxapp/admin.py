from django.contrib import admin
from .models import Taxpayer,Bank,Citizen


class ServiceAdmin(admin.ModelAdmin):
    list_display=('pk','name','nid')
admin.site.register(Taxpayer,ServiceAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('pk','name','nid')
admin.site.register(Citizen,ServiceAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('pk','bname','nid','balance','acno',)
admin.site.register(Bank,ServiceAdmin)
