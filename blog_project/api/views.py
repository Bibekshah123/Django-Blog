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
from rest_framework import generics

# Create your views here.

class BlogListCreateApiView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
class BlogUpdateDeleteApiView(generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
class BlogRetrieveApiView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    

#comment api view
class CommentListCreateApiView(generics.ListAPIView, generics.CreateAPIView,):
    queryset = Comment.objects.all()
    serializer_class = BlogCommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
class CommentReadApiView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = BlogCommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    # def get(self, request):
    #     comment = Comment.objects.all()
    #     serializer = BlogCommentSerializer(comment, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = BlogCommentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

        