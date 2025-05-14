from rest_framework import serializers
from blog_app.models import Post, Comment
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image',  'content', 'author', 'created_at']
        
class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'body']
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#          model = User
#          fields = ['id', 'username', 'email']
         
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
        
#         def post(self, validate)