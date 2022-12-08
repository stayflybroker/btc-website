# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'broker/home.html')

def about(request):
    return render(request, 'broker/about.html', {'title': 'About Us'})
    
def reviews(request):
    return render(request, 'broker/reviews.html', {'title': 'More reviews'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Congratulations {user.first_name}! Your account has been successfully created, make a deposit to get started and see an active balance!')
            return redirect('broker-portfolio')
    else:
        form = UserRegisterForm()
    return render(request, 'broker/register.html', {'form': form})


@login_required
def deposit(request):
    return render(request, 'broker/deposit.html', {'title': 'Deposit and get started'})
@login_required
def withdraw(request):
    return render(request, 'broker/withdraw.html', {'title': 'Withdraw'})
@login_required
def done(request):
    return render(request, 'broker/done.html', {'title': 'Done'})
@login_required
def portfolio(request):
    return render(request, 'broker/portfolio.html', {'title': 'Portfolio'})

