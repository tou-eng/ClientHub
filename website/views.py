from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def index(request):
    #Check if the user is authenticated
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('index')
    else:
        return render(request, 'index.html',{})

# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')
def register_user(request):
    return render(request, 'register.html',{})