from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog_list.html'

    def get_queryset(self):
        queryset = Post.objects.all()
        user_title = self.request.GET.get('query')

        if user_title:
            queryset = queryset.filter(title__icontains=user_title)

        return queryset
# user_title = "my title"
# blogs = Blog.objects.filter(title=user_title)
# first_blog_post = blogs.first()
# last_blog_post = blogs.last()
# latest_blog_post = blogs.latest('id')
