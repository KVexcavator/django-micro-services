import subprocess
from django.core.management.base import BaseCommand
from subscription_registration.mongo_init import init_db

class Command(BaseCommand):
    help = "Run ASGI server via uvicorn"
    def handle(self, *args, **options):
        subprocess.run([
            "uvicorn",
            "subscription_registration.asgi:application",
            "--reload",
            "--host", "0.0.0.0",
            "--port", "8000"
        ])
