from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        if users.exists():
            for user in users:
                self.stdout.write(user.username)
        else:
            self.stdout.write("no user found!!!")