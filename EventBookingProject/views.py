from django.shortcuts import render


def home(request):
    return render(request, template_name='index.html')


def speakers(request):
    return render(request, template_name='speakers.html')


def schedule(request):
    return render(request, template_name='schedule.html')


def sponsors(request):
    return render(request, template_name='sponsors.html')


def news(request):
    return render(request, template_name='news-single.html')


def register(request):
    return render(request, template_name='../templates/auth/register.html')


def login(request):
    return render(request, template_name='../templates/auth/login.html')


def logout(request):
    return render(request, template_name='../templates/auth/logout.html')


def contact(request):
    return render(request, template_name='contact.html')
