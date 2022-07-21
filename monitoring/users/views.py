from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Registration
from django.contrib.auth.models import User
from home.models import Monitoring
from django.db.models import F

def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            reg_user = User.objects.get(username=username)
            if Monitoring.objects.filter(day=reg_user.date_joined).exists():
                monitor = Monitoring.objects.filter(day=reg_user.date_joined)
                monitor.update(count=F('count') + 1)
            else:
                monitor = Monitoring(day=reg_user.date_joined, count=1)
                monitor.save()
            return redirect('auth')
    else:
        form = Registration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
