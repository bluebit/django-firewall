== Django Firewall ==

Django Firewall is a Django middleware that lets you block visitors from accessing parts of your website. Maybe you're low on resources and need to temporarily block visitors from visiting certain pages, or you want to test something with your templates and don't want visitors to see the changes yet. Whatever the reason is, Django Firewall will let you, easily and quickly, show your visitors they have reached a restricted area.

One of the uses is if you want to set up a "beta" section on your website and give certain users access to it.

Features:
    * Block and unblock on predetermined times.
    * You can block your whole website or just parts of it.
    * Show your visitors static HTML or redirect your visitors to another page/site.
    * Admins won't be affected by the block (obviously).
    * Specify paths that you want blocked (like /faq, /restricted/area).

Django Firewall requires the django.contrib.auth app because it needs to create firewall permissions.

For authorization, Django Firewall checks if the user is logged in first, then checks if the user has permission to access blocked paths. If these conditions are met, Django Firewall will let the user through.

REQUIREMENTS:
1. django.contrib.auth app must be installed.
2. django.contrib.admin app must be installed.

INSTALLATION:
1. Download the firewall app and put it in your project's folder.
2. Add the app to your INSTALLED_APPS in your settings.py.
3. Add 'project.firewall.middleware.FirewallMiddleware' to the MIDDLEWARE_CLASSES in your settings.py file. The middleware class must come AFTER the authorization middleware because it depends on it. Replace 'project' with your project name.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'project.firewall.middleware.FirewallMiddleware',
)
4. Run ./manage.py syncdb

That's it.

Django Firewall is still in its very early stages and if anyone has any suggestions or feedback, they are very welcome.