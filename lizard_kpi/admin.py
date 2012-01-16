from django.contrib import admin

from lizard_kpi.models import KPI
from lizard_kpi.models import KPIPage


class KPIPageAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'description']
    list_editable = ['name', 'description']


class KPIAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'url', 'kpi_page', 'order']
    list_editable = ['value', 'url', 'kpi_page', 'order']


admin.site.register(KPI, KPIAdmin)
admin.site.register(KPIPage, KPIPageAdmin)
