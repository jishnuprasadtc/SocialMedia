from django.forms.models import BaseModelForm
from socialmedia.models import UserProfile,Post,Comment
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django. views.generic import View,CreateView,FormView,TemplateView,DetailView,ListView
from django.urls import reverse_lazy
from socialmedia.forms import LoginForm,Registration,StudentProfileForm,PostForms,CommentForm
from socialmedia import forms
from django.contrib import messages
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
                return redirect('index1')
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


class UserProfilecreate(CreateView):
    template_name="userprofile.html"
    form_class=StudentProfileForm
    success_url=reverse_lazy("index1")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class Profile(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=UserProfile.objects.get(id=id)
        return render(request,"profile.html",{"data":qs})
    


# --Post
    

class PostView(CreateView):
    template_name="Poster.html"
    form_class=PostForms
    model=Post
    success_url =reverse_lazy('post')


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
        
class PostList(ListView):
    template_name="index1.html"
    model=Post
    context_object_name="data"


class PostdeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Post.objects.filter(id=id).delete()
        return redirect("")
    


class CommentCreateView(View):
    def get(self,request,*args,**kwargs):
        form=CommentForm()
        id=kwargs.get("pk")
        Comment_obj=Comment.objects.filter(post=id)
        return render(request,"comment.html",{"form":form,"comment":Comment_obj})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post_obj=Post.objects.get(id=id)
        Comment_obj=Comment.objects.filter(post=id)
        form=CommentForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.instance.post=post_obj
            form.save()
            return render(request,"comment.html",{"form":form,"comment":Comment_obj})


    



