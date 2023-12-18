from django.shortcuts import render,redirect
from django. views.generic import View,CreateView,FormView,TemplateView
from django.urls import reverse_lazy
from socialmedia.forms import LoginForm,Registration,StudentProfileForm
from socialmedia import forms
from django.contrib.auth import authenticate,login,logout


# Create your views here.


class LogininView(FormView):
    template_name="Login.html"
    form_class=LoginForm


    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            psw=form.cleaned_data.get("password")
            userobject=authenticate(request,username=uname,password=psw)
            if userobject:
                login(request,userobject)
                print("success")
                return redirect('index')
            else:
                    return redirect('Signin')
        print("faild")
        return render(request,"login.html",{"form":form})
    


class SignUpView(CreateView):
    template_name="reg.html"
    form_class=Registration
    success_url=reverse_lazy("Signin")


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('Signin')


class IndexView(TemplateView):
    template_name="index.html"


class UserProfilecreate(View):
    def get(self,request,*args,**kwargs):
        form=StudentProfileForm
        return render(request,"userprofile.html",{"form":form})

    # template_name="userprofile.html"
    # form_class=UserProfile
    # success_url=reverse_lazy('index')




