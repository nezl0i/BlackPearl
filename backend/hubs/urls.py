from django.urls import path
from hubs.views import index, design, contact, faq, marketing, mobile, webpage, about

app_name = 'hubs'

urlpatterns = [
    path('', index, name='index'),
    path('design/', design, name='design'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('marketing/', marketing, name='marketing'),
    path('mobile/', mobile, name='mobile'),
    path('web/', webpage, name='webpage'),
    path('about/', about, name='about'),
]
