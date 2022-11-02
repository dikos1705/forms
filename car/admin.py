from django.contrib import admin
from .models import *

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('mark','model', 'is_published','time_create','photo')
    # list_display_links = ('id',)
    search_fields = ('mark','model') 


admin.site.register(Car,CarAdmin)
