from users.views import login
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
]
