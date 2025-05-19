from django.core.management.base import BaseCommand
from blog_app.models import *

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        if posts.exists():
            for post in posts:
                self.stdout.write(f"{post.id} - {post.title} - (Author: {post.author})")
        else:
            self.stdout.write("No post found!!!")
                