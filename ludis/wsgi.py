"""
WSGI config for ludis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

port = os.environ.get('PORT', '8000') 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ludis.settings')

application = get_wsgi_application()

app = application
