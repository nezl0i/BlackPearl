from django.contrib.auth import authenticate, login
from users.forms import LoginForm, SignUpForm
from django.shortcuts import render, redirect
from django.contrib import messages


def login_page(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, 'Некорректные данные')
        else:
            messages.error(request, 'Ошибка в веденных данных')
    context = {
        'title': 'Вход',
        'form': form
    }

    return render(request, "login.html", context)


def register_user(request):
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            messages.info(request, 'Пользователь создан успешно')
            success = True
            return redirect("/login/")
        else:
            messages.error(request, 'Проверьте правильность введенных данных')
    else:
        form = SignUpForm()
    context = {
        'title': 'Регистрация',
        'form': form,
        'success': success
    }

    return render(request, "sign_in.html", context)
