from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    path('', include('hubs.urls', namespace='hubs')),
]
