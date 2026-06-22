from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import signup_form,create_account_form,money_transfer_form
import random
from .models import CreateAccount
from decimal import Decimal

def home(request):
    exits = None

    if request.user.is_authenticated:
        exits = CreateAccount.objects.filter(user=request.user).first()

    return render(request,'app/home.html',{'exits': exits})

@login_required
def services_view(request):
    exits=CreateAccount.objects.filter(user=request.user).first()
    bal=exits.balance
    return render(request,'app/services.html',{'exits':exits,'bal':bal})


def signup_view(request):
    form=signup_form()
    if request.method=='POST':
        form=signup_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'app/signup.html',{'form':form})


def gen_account():
   return "".join(str(random.randint(0,9)) for _ in range(12))



def create_acount_view(request):
    form=create_account_form()
    if request.method=='POST':
        form=create_account_form(request.POST)
        if form.is_valid():
            frm=form.save(commit=False)
            frm.account_number=gen_account()
            frm.user=request.user
            frm.save()
            return redirect('services')
    return render(request,'app/createaccount.html',context={'form':form})


def object_access(request):
    return CreateAccount.objects.filter(user=request.user).first()


def deposit_view(request):
    money=Decimal(request.POST.get('amount'))
    current_user=object_access(request)
    current_user.balance=current_user.balance+money
    current_user.save()
    return redirect('services')


def withdraw_view(request):
    money = Decimal(request.POST.get('amount'))
    current_user = object_access(request)
    if current_user.balance >= money:
        current_user.balance = current_user.balance - money
        current_user.save()
    return redirect('services')


def profile_view(request):
    data=object_access(request)
    return render(request,'app/profile.html',{'d':data})

def loans(request):pass

def services_main_view(request):
    return render(request,'app/options.html')


def money_transfer_view(request):
    form=money_transfer_form()
    return render(request,'app/money_transfer_form.html',{'form':form})