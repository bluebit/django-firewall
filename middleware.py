from django.http import HttpResponseRedirect
from firewall.models import Firewall
import datetime

class FirewallMiddleware():
    def process_request(self, request):
        now = datetime.datetime.now()
        
        # Let admins through.
        if request.user.is_authenticated() and request.user.is_active and request.user.is_staff:
            return None
        
        # Let users with permissions through
        if request.user.is_authenticated() and request.user.is_active and request.user.has_perm('firewall.can_access'):
            return None
        
        try:
            fw = Firewall.objects.get(
                is_active=True,
                start_on__lte=now,
                stop_on__gte=now)
            blocked_paths = fw.blocked_paths.split(',')
            blocked_paths = tuple([p.strip() for p in blocked_paths])
            if request.path.startswith(blocked_paths):
                return HttpResponseRedirect(fw.redirect_to_url)
        except:
            return None