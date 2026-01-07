from django.urls import path
from . import views
from .views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]