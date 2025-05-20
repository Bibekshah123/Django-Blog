from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = "shows all middleware that are in my settins.py"
    
    def handle(self, *args, **kwargs):
        print("----Middleware--- \n")
        for i in settings.MIDDLEWARE:
            print(i)