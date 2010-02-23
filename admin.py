from django.contrib import admin
from firewall.models import Firewall
from firewall.forms import FirewallForm

class FirewallAdmin(admin.ModelAdmin):
    list_display = ('explanation', 'is_active', 'start_on', 'stop_on', 'blocked_paths',)
    list_filter = ('is_active', 'start_on', 'stop_on',)
    search_fields = ('explanation', 'blocked_paths',)
    list_editable = ('is_active', 'start_on', 'stop_on', 'blocked_paths',)
    
    form = FirewallForm

admin.site.register(Firewall, FirewallAdmin)
