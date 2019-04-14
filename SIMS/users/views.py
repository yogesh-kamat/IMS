from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from users.forms import LoginForm

def index(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                context = {
                    'form':loginform,
                    'error':'Could not login, Please try again...',
                }
                return render(request, 'users/index.html', context)  
    loginform = LoginForm()
    context = {
        'form' : loginform,
    }
    return render(request,'users/index.html', context)

def logout_user(request):
    logout(request)
    return redirect(reverse('login'))