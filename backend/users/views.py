from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.models import User
from users.forms import LoginForm, SignUpForm, ProfileForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Авторизация'
        return context_data


class UserLogoutView(LogoutView):
    template_name = 'index.html'


class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')
    # fields = ('username', 'email', 'first_name', 'about_me')

    def get_success_url(self):
        return reverse('users:profile', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user_id = self.kwargs.get('pk')
        # user_item = get_object_or_404(User, pk=user_id)
        context['title'] = 'Профиль'
        return context


class UserRegistrationView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'users/sign_in.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Регистрация'
        return context_data

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        if form.is_valid():
            user = form.save()
        return super().form_valid(form)
