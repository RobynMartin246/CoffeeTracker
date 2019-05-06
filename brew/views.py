from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from django.utils import timezone


from .forms import BrewForm, RoastForm
from .models import Brew, Roast, Acidity, Flavor


def index(request):
    return render(request,'brew/index.html')

@login_required    
def new_brew(request):
    if request.method == 'POST':
        form = BrewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.pub_date = timezone.now()
            obj.save()
            form.save_m2m()
            return redirect('brew:profile')
    else:
        form = BrewForm()
    return render(request, 'brew/new_brew.html', {'form': form})

def update_brew(request, brew_id): 
    brew = get_object_or_404(Brew, pk=brew_id)
    if request.method == "POST":
        form = BrewForm(request.POST, instance=brew)
        if form.is_valid():
            brew = form.save(commit=False)
            brew.user = request.user
            brew.pub_date = timezone.now()
            brew.save()
            form.save_m2m()
            return redirect('brew:brew_profile', brew_id)
    else:
        form = BrewForm(instance=brew)
    return render(request, 'brew/brew_update_form.html', {'form': form})  

def brew_delete(request, brew_id):
    brew = get_object_or_404(Brew, pk=brew_id)
    if request.method == 'POST':
        brew.delete()
        return HttpResponseRedirect("/profile/")
    return render(request, 'brew/brew_confirm_delete.html', {'brew': brew})

@login_required  
def brew_profile(request, brew_id):
    brew = get_object_or_404(Brew, pk=brew_id)
    return render(request,'brew/brew_profile.html', {'brew': brew})

def new_roast(request):
    if request.method =='POST':
        form = RoastForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            return redirect('brew:profile')
    else:
        form = RoastForm()
    return render(request, 'brew/new_roast.html', {'form': form})

def roast_profile(request, roast_id):
    roast = get_object_or_404(Roast, pk=roast_id)
    return render(request, 'brew/roast_profile.html', {'roast': roast})

def update_roast(request, roast_id): 
    roast = get_object_or_404(Roast, pk=roast_id)
    if request.method == "POST":
        form = RoastForm(request.POST, instance=roast)
        if form.is_valid():
            roast = form.save(commit=False)
            roast.user = request.user
            roast.save()
            form.save_m2m()
            return redirect('brew:roast_profile', roast_id)
    else:
        form = RoastForm(instance=roast)
    return render(request, 'brew/roast_update_form.html', {'form': form})  

def roast_delete(request, roast_id):
    roast = get_object_or_404(Roast, pk=roast_id)
    if request.method == 'POST':
        roast.delete()
        return HttpResponseRedirect("/profile/")
    return render(request, 'brew/roast_confirm_delete.html', {'roast': roast})

@login_required
def profile(request):
    brew_list = Brew.objects.filter(user=request.user).order_by('-pub_date')[:10]
    roast_list = Roast.objects.filter(user=request.user).order_by('-pub_date')
    return render(request, 'brew/profile.html', {'brew_list': brew_list, 'roast_list': roast_list})

def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            registered = True
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('brew:profile')
        else:
            print('error')
    else:
        form = UserCreationForm()

    return render(request, 'brew/register.html', {'form': form})


'''
def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user=form.user_name(request)

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/profile/')
    else:
        form = LoginForm()

    return render(request, 'brew/login.html', {'form': form})
'''


