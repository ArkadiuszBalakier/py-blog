from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by('-created_time')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'