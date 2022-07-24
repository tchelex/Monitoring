from django.contrib import admin
from .models import Monitoring

class MonitoringAdmin(admin.ModelAdmin):
    list_display = ('day', 'count')



admin.site.register(Monitoring, MonitoringAdmin)
