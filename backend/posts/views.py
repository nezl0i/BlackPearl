from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from .models import Post, Category, Comment
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView, FormMixin
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404


def index(request):
    content = {
        'title': 'Блог статей команды BlackPearl>',
        'description': 'Интересные статьи обо всем. Популярные рубрики и занимательный контент.'
    }
    return render(request, 'index.html', content)


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


class CreatePostView(FormView):
    """
    View for Post creation
    Field author hidden, we get it from :request
    """
    form_class = PostForm
    template_name = 'posts/create-post.html'

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('posts:index'))
        return HttpResponseRedirect(reverse('posts:create-post'), kwargs={'form': form})


class UpdatePostView(UpdateView):
    """
    Class Based view for update Post
    :pk post needed
    """
    model = Post
    form_class = PostForm
    template_name = 'posts/create-post.html'
    success_url = '/me/posts'


class DeletePostView(DeleteView):
    """
    Class Based view for delete Post
    :pk post needed
    """
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = '/me/posts'


class MyPostsView(ListView):
    """
    Class Based view for show user posts
    :pk user needed
    """
    template_name = 'posts/myposts.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Post.objects.filter(author=self.request.user)
        return context


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)


class PostFullView(CustomSuccessMessageMixin, FormMixin, DetailView):
    """
    Class Based details view for Post
    :slug post needed 
    """
    model = Post
    form_class = CommentForm
    template_name = 'posts/postview.html'
    success_url = reverse_lazy('posts:index')
    success_msg = 'Комментарий создан, ожидайте модерации'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post=kwargs.get("object"), active=True)
        context['comments'] = comments
        return context

    def get_success_url(self):
        return reverse_lazy('posts:full-post', kwargs={'slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CategoryPostsView(TemplateView):
    """
    Class Based view for show all Posts or filtered by category
    :category name needed for filtering

    """

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if kwargs.get('category'):
            try:
                context["object_list"] = Post.objects.filter(
                    id_category__name=kwargs.get('category'))
                context['title'] = kwargs.get('category')
                context['description'] = Category.objects.filter(name=kwargs.get('category')).values()[0]['description']
            except (TypeError, KeyError):
                context["object_list"] = []
        else:
            context["object_list"] = Post.objects.all()
            context['title'] = 'Блог статей команды BlackPearl'
            context['description'] = 'Интересные статьи обо всем. Популярные рубрики и занимательный контент.'

        return context
