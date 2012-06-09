#!/opt/python27/bin/python2.7
import os
import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'vpnauth.settings'
application = django.core.handlers.wsgi.WSGIHandler()
