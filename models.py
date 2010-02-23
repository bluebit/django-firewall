from django.db import models

class Firewall(models.Model):
    is_active = models.BooleanField(default=False)
    start_on = models.DateTimeField()
    stop_on = models.DateTimeField()
    explanation = models.CharField(max_length=200, unique=True,
        help_text='For you. To remember what this firewall is for. This field must be unique.')
    blocked_paths = models.CharField(max_length=200, default='/example',
        help_text='A comma separated list of paths that will be blocked. (e.g. /beta, /vip/only)')
    redirect_to_url = models.URLField(u'Redirect to URL',
        help_text='Where to redirect unauthorized visitors.'
            ' Can be relative (/home) or fully qualified (http://google.com)')
    
    class Meta:
        ordering = ('is_active', 'start_on',)
        permissions = (
            ('can_access', 'Can access firewalled paths'),
        )
    
    def __unicode__(self):
        return self.explanation
