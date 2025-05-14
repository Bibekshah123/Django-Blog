from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
import itertools 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=False)
    # like_count = models.PositiveIntegerField(default=0)
    # dislike_count = models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Auto-generate if empty
            self.slug = slugify(self.title)
            # Ensure uniqueness
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{Post.objects.count() + 1}"
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
            
    # def like_count(self):
    #     return self.reactions.filter(reaction='like').count()

    # def dislike_count(self):
    #     return self.reactions.filter(reaction='dislike').count()


# class PostReaction(models.Model):
#     REACTION_CHOICES = [
#         ('like', 'Like'),
#         ('dislike', 'Dislike'),
#     ]
#     post = models.ForeignKey(Post, related_name='reactions', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=40, null=True, blank=True)
#     reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)

#     class Meta:
#         unique_together = ('post', 'user', 'session_key')  # only one reaction per post
    

    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username if self.user else "Anonymous"}'