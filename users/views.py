from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Registration


def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('auth')
    else:
        form = Registration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
