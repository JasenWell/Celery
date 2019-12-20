"""
WSGI config for Celery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.insert(0,root_path)
os.environ["DJANGO_SETTINGS_MODULE"] = 'Celery.settings'
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery.settings')

application = get_wsgi_application()
