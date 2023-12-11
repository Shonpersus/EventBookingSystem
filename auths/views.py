from django.shortcuts import render
from auths.models import Users
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        if (request.POST.get('name') and request.POST.get('email') and request.POST.get('password') and
                request.POST.get('phone') and request.POST.get('ticket_type')):
            saverecord = Users
            saverecord.name = request.POST.get('name')
            saverecord.name = request.POST.get('email')
            saverecord.name = request.POST.get('password')
            saverecord.name = request.POST.get('phone')
            saverecord.name = request.POST.get('ticket_type')
            saverecord.save()
            messages.success(request, 'You Have Registered Successfully...!')
        return render(request, 'auth/register.html')
    else:
        return render(request, 'index.html')


