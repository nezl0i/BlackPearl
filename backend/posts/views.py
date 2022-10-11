
from django.contrib.auth import authenticate, login
from users.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages

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


def login(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, 'Некорректные данные')
                # msg = 'Некорректные данные'
        else:
            # msg = 'Ошибка в веденных данных'
            messages.error(request, 'Ошибка в веденных данных')
    context = {
        'title': 'Вход',
        'msg': msg,
        'form': form
    }

    return render(request, "login.html", context)
# def login(request):
#     content = {
#         'title': 'Авторизация',
#     }
#     return render(request, 'login.html', content)
