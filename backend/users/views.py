from django.contrib.auth import authenticate, login
from users.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages


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
