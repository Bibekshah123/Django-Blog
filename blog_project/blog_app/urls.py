from django.urls import path
from .views import *
from api.views import *

urlpatterns = [
    
    #login
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    #api
    path('blog/', BlogListCreateApiView.as_view()),
    path('blog/updatedelete/<int:pk>/',  BlogUpdateDeleteApiView.as_view()),
    path('blog/retrieve/<int:pk>/', BlogRetrieveApiView.as_view()),
    
    path('', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    #api
    path('comment-list-create/', CommentListCreateApiView.as_view()),

]
