from vpn.models import VpnLog
from django.contrib import admin

class VpnLogAdmin(admin.ModelAdmin):
    list_display = ['username','content','login_time','result']
    list_filter = ['login_time','result']
    search_fields = ['username']

admin.site.register(VpnLog, VpnLogAdmin)
