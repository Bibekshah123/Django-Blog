from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment, PostReaction
from .forms import PostForm, CommentForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

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
    # paginate_by = 6
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

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
            return redirect('post_detail', slug=self.object.slug)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


        
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'image', 'content']  
    success_url = reverse_lazy('post_list') 

    def form_valid(self, form):
        form.instance.author = self.request.user
        
        # Auto-generate slug from title
        if not form.instance.slug:  # Extra safety check
            base_slug = slugify(form.instance.title)
            unique_slug = base_slug
            counter = 1
            
            # Ensure slug is unique
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            form.instance.slug = unique_slug
        return super().form_valid(form)

    def get_success_url(self):
        # After form_valid(), self.object contains the saved instance
        if hasattr(self, 'object') and self.object.slug:
            return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})
        return self.success_url  # Fallback if something went wrong
    
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


    
# class PostReactView(View):
#     def post(self, request, slug, action):
#         post = get_object_or_404(Post, slug=slug)
#         cookie_name = f'post_{post.id}_reaction'

#         # Check if user has already reacted
#         if request.COOKIES.get(cookie_name):
#             return redirect('post_detail', slug=slug)  # Already reacted

#         # Update like/dislike count
#         if action == 'like':
#             post.like_count += 1
#             post.save()
#         elif action == 'dislike':
#             post.dislike_count += 1
#         post.save()

#         response = HttpResponseRedirect(reverse('post_detail', kwargs={'slug': slug}))
#         response.set_cookie(cookie_name, action, max_age=365*24*60*60)  # Expires in 1 year

#         return response