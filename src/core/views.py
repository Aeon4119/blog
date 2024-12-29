from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

class BlogListView(ListView):
    model = Blog
    template_name = 'core/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'core/blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'core/blog_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'subtitle', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/pages/'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author