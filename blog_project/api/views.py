from django.shortcuts import render
from rest_framework import viewsets
from blog_app import models
from .serializers import BlogSerializer, BlogCommentSerializer
from rest_framework.views import APIView
from blog_app.models import Post, Comment
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = models.Post.objects.all()
#     serializer_class = BlogSerializer


class BlogListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blog = Post.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)


class BlogCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  # if you track authorship
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        blog = get_object_or_404(Post, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)


class BlogUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        blog = get_object_or_404(Post, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        blog = get_object_or_404(Post, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

#comment api view
class CommentListView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = BlogCommentSerializer(comment, many=True)
        return Response(serializer.data)
    
class CommentCreateView(APIView):
    def post(self, request):
        serializer = BlogCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentDetailList(APIView):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = BlogCommentSerializer(comment)
        return Response(serializer.data)
    

        

        