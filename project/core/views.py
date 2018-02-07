from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from core.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

## USER AUTHENTICATION
def dashboard(request):
    return render(request, 'core/dashboard.html', context={})

def login_user(request):
    next = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],
                    password = request.POST['password'])
            if user is not None:
                login(request, user)
                try:
                    next = request.POST['next']
                    return redirect(next)
                except:
                    next = 'dashboard'
                    return redirect(next)

            else:
                messages.add_message(request, messages.ERROR, 'Failed to authenticate.')
                return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to authenticate.')
            return redirect('login')
    else:
        form = LoginForm()
        try:
            next = request.GET['next']
        except:
            next = None
        return render(
                request,
                'core/login.html',
                context={
                    'form': form,
                    'next': next
                    }
                )

def register_user(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    request.POST['username'],
                    request.POST['email'],
                    request.POST['password'],
                    )
            user.save()
            print("Saved notification for user: " + user.username)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(
            request,
            'core/register.html',
            context={
                'form': form
                }
            )


def logout_user(request):
    logout(request)
    return redirect('login')
