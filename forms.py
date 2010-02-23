from django import forms
from firewall.models import Firewall

class FirewallForm(forms.ModelForm):
    class Meta:
        model = Firewall
    
    def clean_start_on(self):
        start_on = self.cleaned_data['start_on']
        is_active = self.cleaned_data.get('is_active', '')
        if is_active:
            try:
                Firewall.objects.get(is_active=True,
                    start_on__lte=start_on, stop_on__gte=start_on)
                raise forms.ValidationError("There's already an active Firewall that"
                    " conflicts with this Firewall's start_on date/time.")
            except Firewall.DoesNotExist:
                pass
        return start_on
    
    def clean_stop_on(self):
        stop_on = self.cleaned_data['stop_on']
        is_active = self.cleaned_data.get('is_active', '')
        if is_active:
            try:
                Firewall.objects.get(is_active=True,
                    start_on__lte=stop_on, stop_on__gte=stop_on)
                raise forms.ValidationError("There's already an active Firewall that"
                    " conflicts with this Firewall's stop_on date/time.")
            except Firewall.DoesNotExist:
                pass
        return stop_on
