from django.contrib import admin

from lizard_kpi.models import KPI


class KPIAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'url']
    list_editable = ['value', 'url']


admin.site.register(KPI, KPIAdmin)
