from django.urls import path
from .views import PostViewSet, CommentViewSet

post_list = PostViewSet.as_view
({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view
({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

comment_list = CommentViewSet.as_view
({
    'get': 'list',
    'post': 'create'
})
comment_detail = CommentViewSet.as_view
({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('posts/', post_list, name='post-list'),
    path('posts/<int:id>/', post_detail, name='post-detail'),
    path('posts/<int:post_id>/comments/', comment_list, name='comment-list'),
    path('posts/<int:post_id>/comments/<int:id>/', comment_detail, name='comment-detail'),
]