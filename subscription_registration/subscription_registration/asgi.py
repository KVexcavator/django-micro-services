import os
import django
from django.core.asgi import get_asgi_application
import asyncio
from subscription_registration.mongo_init import init_db

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'subscription_registration.settings')
django.setup()
application = get_asgi_application()

loop = asyncio.get_event_loop()
loop.create_task(init_db())


