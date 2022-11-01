from django.urls import path
from django.contrib.auth.decorators import login_required
from posts.views import contact, faq, about, publicate_post, publicate_comment, delete_comment
from .views import CreatePostView, UpdatePostView, DeletePostView, MyPostsView, PostFullView, CategoryPostsView, ModeratePostsView
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'posts'

urlpatterns = [
    path('', CategoryPostsView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('about/', about, name='about'),
    path('category/<str:category>/', CategoryPostsView.as_view(), name='category-posts'),
    path('create-post/', login_required(CreatePostView.as_view()), name='create-post'),
    path('edit-post/<int:pk>', login_required(UpdatePostView.as_view()), name='update-post'),
    path('delete-post/<int:pk>', login_required(DeletePostView.as_view()), name='delete-post'),
    path('me/posts/', MyPostsView.as_view(), name='myposts'),
    path('post/<str:slug>', PostFullView.as_view(), name='full-post'),
    path('moderate/posts/', staff_member_required(ModeratePostsView.as_view()), name='mod-posts'),
    path('post/publicate/<int:pk>/', publicate_post, name='pub-post'),
    path('comment/publicate/<int:pk>/', publicate_comment, name='pub-comment'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete-comment'),
]
