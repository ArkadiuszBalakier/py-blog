from django.shortcuts import render

from blog.models import Post


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {
        "post_list": post_list,
    }
    return render(request, 'blog/index.html', context=context)