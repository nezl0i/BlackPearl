
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from .models import Post
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import PostForm
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'index.html')


def contact(request):
    content = {
        'title': 'Контакты',
        'description': 'Lorem ipsum dolor amet consecrate adipiscing dolore magna aliqua '
                       'enim minim estudiat veniam siad venomous dolore'
    }
    return render(request, 'contact.html', content)


def design(request):
    content = {
        'title': 'Дизайн',
        'description': 'Lorem ipsum dolor amet consecrate adipiscing dolore magna aliqua '
                       'enim minim estudiat veniam siad venomous dolore'
    }
    return render(request, 'design.html', content)


def faq(request):
    content = {
        'title': 'Часто задаваемые вопросы',
        'description': 'Lorem ipsum dolor amet consecrate adipiscing dolore magna aliqua '
                       'enim minim estudiat veniam siad venomous dolore'
    }
    return render(request, 'faq.html', content)


def marketing(request):
    content = {
        'title': 'Маркетинг',
        'description': 'Lorem ipsum dolor amet consecrate adipiscing dolore magna aliqua '
                       'enim minim estudiat veniam siad venomous dolore'
    }
    return render(request, 'marketing.html', content)


def mobile(request):
    content = {
        'title': 'Мобильная разработка',
        'description': 'Lorem ipsum dolor amet consecrate adipiscing dolore magna aliqua '
                       'enim minim estudiat veniam siad venomous dolore'
    }
    return render(request, 'mobile_dev.html', content)


def webpage(request):
    content = {
        'title': 'Веб разработка',
        'description': 'Lorem ipsum dolor amet consecrate adipiscing dolore magna aliqua '
                       'enim minim estudiat veniam siad venomous dolore'
    }
    return render(request, 'web_dev.html', content)


def about(request):
    content = {
        'title': 'О нас',
        'description': 'Lorem ipsum dolor amet consecrate adipiscing dolore magna aliqua '
                       'enim minim estudiat veniam siad venomous dolore'
    }
    return render(request, 'about.html', content)


class TestPosts(ListView):
    template_name = 'posts/allposts.html'
    model = Post


class CreatePostView(FormView):
    form_class = PostForm
    template_name = 'create-post.html'

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('posts:allposts'))
        return HttpResponseRedirect(reverse('posts:create-post'), kwargs={'form': form})


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create-post.html'
    success_url = '/me/posts'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = '/me/posts'

class MyPostsView(ListView):
    template_name = 'posts/myposts.html'
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Post.objects.filter(author=self.request.user)
        return context


class PostFullView(DetailView):
    model = Post
    template_name = 'posts/postview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["object"] = get_object_or_404(Post, slug = kwargs["slug"])
        except (TypeError, KeyError):
            pass
        
        return context
    