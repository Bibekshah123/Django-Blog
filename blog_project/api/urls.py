from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
        #api
    path('blog/', BlogListCreateApiView.as_view()),
    path('blog/updatedelete/<int:pk>/',  BlogUpdateDeleteApiView.as_view()),
    path('blog/retrieve/<int:pk>/', BlogRetrieveApiView.as_view()),
    
        #api
    path('comment-list-create/', CommentListCreateApiView.as_view()),
    path('comment-read/<int:pk>.', CommentReadApiView.as_view()),
]




