from django.core.management.base import BaseCommand
from django.conf import model


class Command(BaseCommand):
    help = "show current models"
    
    def handle(self, *args, **kwargs):
        pass
        
