from django.urls import path, include
from likes.views import ajax_like
from posts.views import PostFullView

app_name = 'likes'

urlpatterns = [
    path('likes/', include([
        path('ajax/', ajax_like, name='ajax')
        # path('ajax/', PostFullView.as_view(), name='ajax')
    ])),
]
