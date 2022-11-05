from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from .views import FeedbackView, read_msg, delete_msg

app_name = 'contacts'

urlpatterns = [
    path('feedback/', staff_member_required(FeedbackView.as_view()), name='main'),
    path('feedback/read/<int:pk>/', read_msg, name='read_msg'),
    path('feedback/delete/<int:pk>/', delete_msg, name='delete_msg'),
]
