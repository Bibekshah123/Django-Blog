from django.urls import path
from .views import *
from api.views import *

urlpatterns = [
    
    path('blog/', BlogListCreateView.as_view()),
    path('blog/updatedelete/<int:pk>/',  BlogUpdateDeleteView.as_view()),
    
    # path('', PostListView.as_view(), name='post_list'),
    # path('post/new/', PostCreateView.as_view(), name='post_create'),
    # path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    # path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # path('post/<slug:slug>/<str:action>/', PostReactView.as_view(), name='react_to_post'),
    
    path('comment/', CommentListView.as_view(), name='comment-list'),
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/detail/<int:pk>/', CommentDetailList.as_view(), name='comment-detail'),

]
