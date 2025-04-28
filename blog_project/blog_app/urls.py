from django.urls import path
from .views import PostListView, PostDetailView, post_create, post_update, post_delete, add_comment
from .views import register_view, login_view, logout_view

urlpatterns = [
    
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_update, name='post_update'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),

]
