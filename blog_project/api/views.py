from django.shortcuts import render
from rest_framework import viewsets
from blog_app import models
from .serializers import BlogSerializer, BlogCommentSerializer, UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from blog_app.models import Post, Comment
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

User = get_user_model()


class UserListView(APIView):
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'msg': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
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
class CommentListCreateApiView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = BlogCommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
class CommentReadApiView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = BlogCommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    



        

        