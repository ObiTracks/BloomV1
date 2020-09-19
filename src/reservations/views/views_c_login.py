from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#View imports here
from ..forms import CreateUserForm
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms import *
from ..filters import CustomerFilter
from ..decorators import unauthenticated_user

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')


    context = {}
    return render(request, '../templates/login_templates/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    context = {}
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form
            
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            apt = form.cleaned_data.get('apt')
            raw_password = form.cleaned_data.get('password1')

            # group = Group.objects.get(name='resident')
            # user.groups.add(group)
            # Customer.objects.create(
            #     user=user,
            #     firstname=firstname,
            #     lastname=lastname,
            #     email=email,
            #     apt=apt,
            #     )
            # messages.success(request, 'Account was created for {} {}'.format(firstname,lastname))

            # return redirect('login')
            return redirect('home')
        else:
            context['registration_form'] = form
    else: # This would be a get request
        form = CreateUserForm()
        context['registration_form'] = form

    # context = {'registration_form':registration_form}
    return render(request,'../templates/login_templates/register.html', context)


def profilePage(request):
    
    context = {}
    return render(request, '../templates/login_templates/profile.html', context)