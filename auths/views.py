from django.shortcuts import render
from auths.models import Users
from django.contrib import messages


def register(request):
    if request.method == 'post':
        if (request.POST.get('name') and request.POST.get('email') and request.POST.get('password') and
                request.POST.get('phone') and request.POST.get('ticket_type')):
            saverecord = Users
            saverecord.name = request.POST.get('name')
            saverecord.email = request.POST.get('email')
            saverecord.password = request.POST.get('password')
            saverecord.phone = request.POST.get('phone')
            saverecord.ticket_type = request.POST.get('ticket_type')
            saverecord.save()
            messages.success(request, 'You Have Registered Successfully...!')
        return render(request, 'auth/register.html')
    else:
        return render(request, 'auth/register.html')


def login(request):
    return render(request, template_name='auth/login.html')


def logout(request):
    return render(request, template_name='auth/logout.html')