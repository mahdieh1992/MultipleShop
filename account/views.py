import datetime

from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.views.generic import View
from .forms import FormLoginUser,RegisterUserForm,ForgetPasswordUser
from .models import CustomUser,Restpassuser
from random import randint
from melipayamak import Api
from datetime import datetime,timedelta
from django.contrib import messages
from django.utils.crypto import get_random_string

def RgisterUser(request):
    form=RegisterUserForm()
    if request.method=='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            fir = form.cleaned_data['Firstname']
            print(fir)
            email=form.cleaned_data['email']
            mobile = form.cleaned_data['Mobile']
            nationalcode = form.cleaned_data['NationalCode']
            if CustomUser.objects.filter(email=email).exists():
                form.add_error('email','email is already registered')
            elif CustomUser.objects.filter(Mobile=mobile).exists():
                form.add_error('Mobile', 'Mobile is already registered')
            elif CustomUser.objects.filter(NationalCode=nationalcode).exists():
                form.add_error('NationalCode', 'NationalCode is already registered')
            else:
                user=form.save(commit=False)
                user.Username=user.email
                user.save()
                return redirect('account:login')
    return render(request, 'account/register.html', {
                'form': form})


class LoginUser(View):
    def get(self,request):
        form=FormLoginUser()
        return render(request,'account/login.html',{
            'form':form
        })

    def post(self,request):
        form=FormLoginUser(request.POST)

        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(email=email,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('Home:main')
                form.add_error('email','Your account is blocked')
            elif not CustomUser.objects.filter(email=email).exists():
                form.add_error('email','Your account is not exists')

            elif not CustomUser.objects.filter(password=password).exists():
                form.add_error('email', 'Your Password is wrong')

        return render(request,'account/login.html',{
                'form': form})


def LogoutUser(request):
    logout(request)
    return redirect('account:login')


class ForgetPassView(View):
    def get(self,request):
        form=ForgetPasswordUser()
        return render(request, 'account/ForgetPassword.html', {
            'form': form
        })

    def post(self,request):
        form=ForgetPasswordUser(request.POST)
        if form.is_valid():
            mobile=form.cleaned_data['Mobile']
            if CustomUser.objects.filter(Mobile=mobile).exists():
                rand=randint(10000,99999)
                token=get_random_string(length=32)
                now=datetime.now()
                now5=now+timedelta(minutes=2)
                Restpassuser.objects.create(mobile=mobile,code=rand,ExpireTime=now5,token=token)
                username = '09122435833'
                password = 'qweQWE123!@#'
                api = Api(username, password)
                sms = api.sms()
                to = mobile
                _from = '50004001435833'
                text = f'Your code is {rand}'
                response = sms.send(to, _from, text)

                return redirect(reverse('account:Confirm')+f'?token={token}')
            form.add_error('Mobile',f'{mobile} is not valid')

        return render(request,'account/ForgetPassword.html',{
            'form':form
        })


class ConfirmCode(View):
    def get(self,request):
        return render(request,'account/Confirm.html',{

        })

    def post(self,request):
        confirmcode=request.POST['code']
        gettoken=request.GET.get('token')
        if Restpassuser.objects.filter(code=confirmcode,token=gettoken).exists():
            return redirect('Home:main')

        messages.info(request,f'{confirmcode} is not valid')
        return render(request, 'account/Confirm.html', {

            })