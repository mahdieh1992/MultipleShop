from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from .forms import FormLoginUser
from .models import CustomUser


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
