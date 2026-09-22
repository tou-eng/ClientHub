from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm
from .models import Record
# Create your views here.
def index(request):

    records = Record.objects.all()
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
        return render(request, 'index.html',{'records':records})

# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered.')
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})


def customer_detail(request, pk):
    if request.user.is_authenticated:
        customere_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customere_record})
    else:
        messages.error(request, 'You must be logged in to view this page.')
        return redirect('index')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record has been deleted successfully.')
        return redirect('index')
    else:
        messages.error(request, 'You must be logged in to delete a record.')
        return redirect('index')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record has been added successfully.')
                return redirect('index')
        return render(request, 'add_record.html', {'form': form})   
    else:
        messages.error(request, 'You must be logged in to add a record.')
        return redirect('index')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record has been updated successfully.')
                return redirect('index')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to update a record.')
        return redirect('index')