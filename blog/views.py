from django.shortcuts import render
from django.views import generic
from .forms import CommentaryForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentaryForm()
        context['comments'] = self.object.comments.all().order_by('-created_time')
        return context