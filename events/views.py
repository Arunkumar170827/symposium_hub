from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Registration
from .forms import RegistrationForm

# --- AUTHENTICATION VIEWS ---

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'events/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST' or request.method == 'GET':
        logout(request)
        return redirect('login')

# --- CRUD OPERATIONS ---

@login_required
def dashboard(request):
    # READ: View only registrations made by the currently logged-in user
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/dashboard.html', {'registrations': registrations})

@login_required
def create_registration(request):
    # CREATE: Register for an event
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.save()
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'events/registration_form.html', {'form': form, 'title': 'New Registration'})

@login_required
def update_registration(request, pk):
    # UPDATE: Edit an existing registration
    registration = get_object_or_404(Registration, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'events/registration_form.html', {'form': form, 'title': 'Update Registration'})

@login_required
def delete_registration(request, pk):
    # DELETE: Cancel a registration
    registration = get_object_or_404(Registration, pk=pk, user=request.user)
    if request.method == 'POST':
        registration.delete()
        return redirect('dashboard')
    return render(request, 'events/registration_confirm_delete.html', {'registration': registration})