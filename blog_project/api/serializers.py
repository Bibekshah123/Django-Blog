from rest_framework import serializers
from blog_app.models import Post, Comment
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField, EmailField, ValidationError


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
        
class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True)
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
        

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