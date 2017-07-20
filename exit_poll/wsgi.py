"""
WSGI config for exit_poll project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/administrador/django/exit_poll')
os.environ['DJANGO_SETTINGS_MODULE'] = 'exit_poll.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


