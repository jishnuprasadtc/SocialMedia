from socialmedia.models import UserProfile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registration(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","email","password1","password2"]
        widgets={
                "username":forms.TextInput({"class":"form-control"}),
                "first_name":forms.TextInput({"class":"form-control"}),
                "email":forms.EmailInput({"class":"form-control"}),
                "password1":forms.TextInput({"class":"form-control"}),
                "password2":forms.TextInput({"class":"form-control"})
            }



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields="__all__"
