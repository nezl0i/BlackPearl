from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from posts.views import contact, faq, about, login
from .views import CreatePostView, UpdatePostView, DeletePostView, MyPostsView, PostFullView, CategoryPostsView

app_name = 'posts'

urlpatterns = [
    path('', CategoryPostsView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('about/', about, name='about'),
    path('category/<str:category>/', CategoryPostsView.as_view(), name='category-posts'),
    # path('testposts/', TestPosts.as_view(), name='allposts'),
    path('create-post/', login_required(CreatePostView.as_view()), name='create-post'),
    path('edit-post/<int:pk>', login_required(UpdatePostView.as_view()), name='update-post'),
    path('delete-post/<int:pk>', login_required(DeletePostView.as_view()), name='delete-post'),
    path('me/posts/', MyPostsView.as_view(), name='myposts'),
    path('post/<str:slug>', PostFullView.as_view(), name='full-post'),

    # path('posts/<str:post-slug>')

    # path('login/', login, name='login'),
]
