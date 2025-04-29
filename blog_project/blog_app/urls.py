from django.urls import path
from .views import *

urlpatterns = [
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # path('post/new/', post_create , name='post_create'),
    # path('post/<int:pk>/edit/', post_update, name='post_update'),
    # path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    # path('post/<int:pk>/comment/', add_comment, name='add_comment'),

]
