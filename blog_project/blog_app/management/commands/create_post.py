from django.core.management.base import BaseCommand
from blog_app.models import *
from django.contrib.auth import get_user_model

User = get_user_model

class Command(BaseCommand):
    help = "creating blog post cmd line"
    
    def add_arguments(self, parser):
        parser.add_argument('title', type=str)
        parser.add_argument('content', type=str)
        parser.add_argument('author_username', type=str)
        parser.add_argument('--publish', action='store_true', help='Publish the post (optional)')
       
    def handle(self, *args, **options):
        title = options['title']
        content = options['content']    
        username = options['author_username']
        publish = options['publish']
        
        try:
            author = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'user "{username}" does not exist.'))
            return
        
        post = Post.objects.create(
            title=title,
            content = content,
            author=author
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created post: "{post.title}"'))
        
    