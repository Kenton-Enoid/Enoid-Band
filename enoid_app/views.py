from django.shortcuts import render, redirect  # new (redirect)
from django.contrib.auth import authenticate, login, logout  # new libraries
from django.contrib.auth.forms import UserCreationForm  # new library
from .models import TourDate    # new library
from .forms import MessageForm      # new library
from django.contrib import messages     # new library
from django.http import HttpResponseRedirect    # new library
from django.urls import reverse     # new library

# Create your views here.
def home(request):
    return render(request, 'home.html')


# Create a view after user signs in
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')


# Create a view for registering users
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Create a view for tour dates
def tour(request):
    tour_dates = TourDate.objects.all()
    return render(request, 'tour.html', {'tour_dates': tour_dates})


# Create a view for contact
def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('contact')
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})

# Create a view if the user decides to log out
def logout_view(request):
    logout(request)
    return redirect('home')