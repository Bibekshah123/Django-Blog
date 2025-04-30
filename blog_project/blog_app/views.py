from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
        return render(request, 'registration/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
        return render(request, 'registration/login.html', {'form': form})
    
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('post_list')



# Blog views
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=self.object.pk)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
        
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'image', 'content']
    success_url = reverse_lazy('post_list')  

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
# Update a post (only author can update)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'image', 'content']
    success_url = reverse_lazy('post_list') 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author 
    

# Delete a post (only author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list') 

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author 
