from django.urls import path
from posts.views import index, design, contact, faq, marketing, mobile, webpage, about, login
from .views import TestPosts

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('design/', design, name='design'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('marketing/', marketing, name='marketing'),
    path('mobile/', mobile, name='mobile'),
    path('web/', webpage, name='webpage'),
    path('about/', about, name='about'),
    path('testposts/', TestPosts.as_view(), name='testpost'),

    # path('login/', login, name='login'),
]
