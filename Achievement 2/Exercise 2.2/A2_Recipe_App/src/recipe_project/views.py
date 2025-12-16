from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    # If user is already logged in, redirect them away from login page
    if request.user.is_authenticated:
        return redirect('recipes:overview')

    error_message = None
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes:overview')  # redirect to protected page
        else:
            error_message = "Oops... something went wrong"

    context = {'form': form, 'error_message': error_message}
    return render(request, 'auth/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('logout-success')   # redirect to success page

def logout_success(request):
    return render(request, 'auth/success.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
