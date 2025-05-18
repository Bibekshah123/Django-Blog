from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('blog/', BlogListCreateView.as_view()),
    path('blog/updatedelet'/'<int:pk>/',  BlogUpdateDeleteView.as_view()),
    
    # #comment url
    path('comment/', CommentListView.as_view(), name='comment-list'),
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/detail/<int:pk>/', CommentDetailList.as_view(), name='comment-detail'),
    
]
