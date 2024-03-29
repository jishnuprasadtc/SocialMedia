from socialmedia.models import UserProfile,Post,Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registration(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","email","password1","password2"]
        widgets={
                "username":forms.TextInput(attrs={"class":"form-control"}),
                "first_name":forms.TextInput(attrs={"class":"form-control"}),
                "email":forms.EmailInput(attrs={"class":"form-control"}),
                "password1":forms.TextInput(attrs={"class":"form-control"}),
                "password2":forms.TextInput(attrs={"class":"form-control"})
            }


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=("user",) 


class PostForms(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","postimage"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
           "postimage":forms.FileInput(attrs={"class":"form-control"})
        }
       

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["title"]