from users.views import login_page, register_user
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_user, name='register'),
]
