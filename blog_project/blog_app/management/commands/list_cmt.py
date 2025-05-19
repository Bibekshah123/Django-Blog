from django.core.management.base import BaseCommand
from blog_app.models import *

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        comments = Comment.objects.all()
        if comments.exists():
            for comment in comments:
                self.stdout.write(f"{comment.id} - {comment.post} - {comment.body} - {comment.user}")
        else:
            self.stdout.write("NO comment found!!!")