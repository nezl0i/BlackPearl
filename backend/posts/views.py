
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from .models import Post
from django.views.generic.edit import FormView
from .forms import PostForm


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
    template_name = 'includes/test-posts.html'
    model = Post


class CreatePostView(FormView):
    form_class = PostForm
    template_name = 'create-post.html'

    # def get_form_kwargs(self):
    #     # pass "user" keyword argument with the current user to your form
    #     kwargs = super(MyFormView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            from transliterate import translit
            import re
            post = form.save(commit=False)
            post.author = request.user
            post.slug = re.sub(r' +','-',translit(post.header, language_code='ru', reversed=True))
            post.save()
            return HttpResponseRedirect(reverse('posts:allposts'))
        return HttpResponseRedirect(reverse('posts:create-post'), kwargs={'form': form})

