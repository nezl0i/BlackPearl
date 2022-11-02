import json
import os

from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView

from backend.settings import EMAIL_HOST_USER
from contacts.forms import ContactForm
from likes.models import PostLikes
from .models import Post, Category, Comment
from django.views.generic.edit import UpdateView, DeleteView, FormMixin, CreateView
from django.views.generic.detail import DetailView
from .forms import PostForm, CommentForm
from django.contrib.admin.views.decorators import staff_member_required

MODULE_DIR = os.path.dirname(__file__)


def faq(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/faq.json')
    context = {
        'title': 'FAQ',
        'description': 'Как работать с BlackPearlCode платформой',
        'faqs': json.load(open(file_path, encoding='utf-8'))
    }

    return render(request, 'faq.html', context)


def about(request):
    content = {
        'title': 'О нас',
        'description': 'О нашей команде BlackPearlCode'
    }
    return render(request, 'about.html', content)


class CreatePostView(CreateView):
    """
    View for Post creation
    Field author hidden, we get it from :request
    """
    form_class = PostForm
    template_name = 'profile/create-post.html'

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
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
    template_name = 'profile/create-post.html'
    success_url = '/me/posts'


class DeletePostView(DeleteView):
    """
    Class Based view for delete Post
    :pk post needed
    """
    model = Post
    template_name = 'profile/delete-post.html'
    success_url = '/me/posts'


class MyPostsView(ListView):
    """
    Class Based view for show user posts
    :pk user needed
    """
    template_name = 'profile/myposts.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).select_related()


class PostFullView(FormMixin, DetailView):
    """
    Class Based details view for Post
    :slug post needed 
    """
    model = Post
    form_class = CommentForm
    template_name = 'posts/postview.html'
    success_url = reverse_lazy('posts:index')
    success_msg = 'Комментарий создан, ожидайте модерации'
    extra_context = {
        'title': 'Статья'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            comments = Comment.objects.filter(
                post=kwargs.get("object"))
        else:
            comments = Comment.objects.filter(
                post=kwargs.get("object"), active=True)

        try:
            post_likes = PostLikes.objects.get(post__id=kwargs.get("object").id, liked_by=self.request.user.id).like
        except (Exception,):
            post_likes = False

        context['comments'] = comments
        context['tags'] = self.object.tags.names()
        context['is_liked'] = post_likes
        return context

    def get_success_url(self):
        return reverse_lazy('posts:full-post', kwargs={'slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, self.success_msg)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CategoryPostsView(ListView):
    """
    Class Based view for show all Posts or filtered by category
    :category name needed for filtering

    """
    model = Post
    template_name = 'index.html'
    success_msg = 'Сообщение отправлено'
    extra_context = {}

    def get_queryset(self):
        if category_title := self.kwargs.get('category'):
            self.extra_context['title'] = category_title
            self.extra_context['description'] = Category.objects.filter(
                name=category_title).values()[0]['description']
            return Post.objects.filter(id_category__name=self.kwargs.get('category'),
                                       status='published').select_related()
        self.extra_context = {
            'title': 'Блог статей команды BlackPearl',
            'description': 'Интересные статьи обо всем. Популярные рубрики и занимательный контент.'
        }

        return Post.objects.filter(status='published').select_related()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, 6)
        page_num = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_num)
        context['form'] = ContactForm()

        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.data
            subject = f'Сообщение с формы от {data["username"]} {data["phone"]} Почта отправителя: {data["email"]}'
            send_mail(subject, data['message'], data["email"], (EMAIL_HOST_USER,))
            # email(subject, data['message'])
            messages.success(self.request, self.success_msg)
            form.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class ModeratePostsView(ListView):
    """
    Class Based view for show user posts
    :pk user needed
    """
    template_name = 'profile/mod-posts.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(status='draft').select_related()


@staff_member_required
def publicate_post(request, pk):
    if request.user.is_staff:
        post = get_object_or_404(Post, pk=pk)
        post.status = 'published'
        post.save()
    return HttpResponseRedirect(reverse('posts:mod-posts'))


@staff_member_required
def publicate_comment(request, pk):
    if request.user.is_staff:
        comment = get_object_or_404(Comment, pk=pk)
        comment.active = True
        comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@staff_member_required
def delete_comment(request, pk):
    if request.user.is_staff:
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
