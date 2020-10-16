from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#View imports here
from ..forms import CreateUserForm
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms import *
from ..filters import CustomerFilter
from ..decorators import unauthenticated_user, allowed_users
from ..tools import *

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            staff_roles = [Group.objects.get(name='SiteAdmin'),Group.objects.get(name='Manager'),Group.objects.get(name='Staff')]
            resident_roles = [Group.objects.get(name='Resident')]
            group = user.groups.all()[0]
            print(group)
            
            if group in staff_roles:
                print("Path A")
                return redirect('/staff')
            else:
                print("Path B")
                return redirect('/user')
            
        else:
            messages.info(request, 'Username or password is incorrect')


    context = {}
    return render(request, '../templates/login_templates/login_templates/login.html', context)


# @login_required(login_url='login')
def registerCompanyPage(request):
    context = {}
    form = CreateCompanyForm()
    if request.method == 'POST':
        form = CreateCompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            
            logout(request)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            apt = 100
            raw_password = form.cleaned_data.get('password')
            
            # user = form.save()
            
            user = Account.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                apt=apt,
                password=raw_password
            )
            
            group = Group.objects.get(name='Manager')
            print(group.user_set.add(user))

            Customer.objects.create(
                user=user,
                company=company,
                first_name=first_name,
                last_name=last_name,
                email=email,
                apt=apt,
                )

            day = Day.objects.create(
                company=company,
                )

            
            TIMESLOTS = TimeSlot.TIMESLOTS
            
            multipleTimeslots(TIMESLOTS, day)
                
            user = authenticate(request, username=email, password=raw_password)
            messages.success(request, 'New company created and managed by {} {}'.format(first_name, last_name))
            
            user = authenticate(request, email=email, password=raw_password)
            return redirect('/staff')
        else:
            context['registration_form'] = form
    else: # This would be a get request
        form = CreateCompanyForm()
        context['registration_form'] = form

    # context = {'registration_form':registration_form}
    template_name = '../templates/login_templates/registration_templates/register_company.html'
    # template_name = 'src/reservations/templates/login_templates/registration_templates/register_company.html'
    return render(request,template_name, context)

    
def registerUserPage(request):
    current_user = request.user
    customer = current_user.customer
    user_company = current_user.customer.company

    form = CreateUserForm()
    LeaseFormSet = inlineformset_factory(Customer, LeaseMember, fields=('full_name','relation'),extra=5)
    form2 = LeaseFormSet(queryset=LeaseMember.objects.none(), instance=customer)

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            apt = form.cleaned_data.get('apt')
            group = form.cleaned_data.get('group')
            print(group)
            raw_password = form.cleaned_data.get('password1')
            
            user = form.save()
            print(user.groups.add(group))

            customer = Customer.objects.create(
                company=user_company,
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                apt=apt,
                )

            messages.success(request, 'Account was created for {} {}'.format(first_name, last_name))

            print(form2.data)
            # return redirect('login')
            return redirect('/staff')
        else:
            # context['registration_form'] = form
            context = {"form":form,"form2":form2}
    else: # This would be a get request
        form = CreateUserForm()
        context = {"form":form,"form2":form2}
        # context['registration_form'] = form

    # context = {'registration_form':registration_form}
    # template_name = '../templates/login_templates/register.html'
    template_name = '../templates/login_templates/registration_templates/register_customer.html'
    return render(request,template_name, context)

def logoutUser(request):
    customer = request.user.customer
    messages.success(request, 'Sucessfully logged out {} {}'.format(customer.first_name, customer.last_name))
    
    logout(request)
    return redirect('/login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager','staff','SiteAdmin'])
def profilePage(request):
    
    context = {}
    return render(request, '../templates/login_templates/profile.html', context)