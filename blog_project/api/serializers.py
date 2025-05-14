from rest_framework import serializers
from blog_app.models import Post, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
        
class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'