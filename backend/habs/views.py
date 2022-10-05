from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def design(request):
    return render(request, 'design.html')


def faq(request):
    return render(request, 'faq.html')


def marketing(request):
    return render(request, 'marketing.html')


def mobile(request):
    return render(request, 'mobile_dev.html')


def webpage(request):
    return render(request, 'web_dev.html')


def about(request):
    return render(request, 'about.html')
