#FILE: roster/admin.py

from django.contrib import admin
from roster.models import Best, Athlete

class BestAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
admin.site.register(Best, BestAdmin)

class AthleteAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
admin.site.register(Athlete, AthleteAdmin)
