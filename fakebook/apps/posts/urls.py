from django.urls import path
from apps.posts.views import *

urlpatterns = [
    path('recommend/', RecommendPostsView.as_view(), name="recommendations"),
    path('create/', CreatePostView.as_view(), name='create_posts'),
    path('remove/', RemovePostView.as_view(), name='remove_posts'),
    path('', GetAllPostsView.as_view(), name='posts'),
]