from django.urls import path
from .views import *
from . import views

urlpatterns = [
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # path('post/<slug:slug>/<str:action>/', PostReactView.as_view(), name='react_to_post'),

]
