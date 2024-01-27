from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    profilepic=models.ImageField(upload_to="image",null=True,blank=True)
    bio=models.CharField(max_length=200)
    dob=models.DateField()
    ph=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="profile")
    city=models.CharField(max_length=200)
    pincode=models.PositiveIntegerField()
    activity=models.CharField(max_length=200)
    supporter=models.CharField(max_length=200)
    
class Post(models.Model):
    user=models.ForeignKey(User,models.DO_NOTHING,related_name="userpost")    
    title=models.CharField(max_length=200)
    postimage=models.ImageField(upload_to="post",null=True,blank=True)
    createddate=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name="likedpost")
    created_at=models.DateTimeField(auto_now=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)




class Comment(models.Model):
    title=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True ,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)