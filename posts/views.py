from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from posts.models import BlogPost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class BlogHomeView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'posts/home.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


@method_decorator(login_required, name='dispatch')
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    fields = ['title', 'content', 'created_on',]


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_update.html'
    fields = ['title', 'content', 'published', ]


class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'posts/blogpost_detail.html'


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    context_object_name = 'post'
    success_url = reverse_lazy('posts:home')
