"""
URL configuration for Socialmediaapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from socialmedia import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path("",views.LogininView.as_view(),name="Signin"),
    path("socialmedia/register/",views.SignUpView.as_view(),name="Sign-up"),
    path("index",views.IndexView.as_view(),name='index'),
    path("Signout",views.SignOutView.as_view(),name="Signout"),
    path("profile/add/",views.UserProfilecreate.as_view(),name="add-profile"),
    path("profile/<int:pk>/",views.Profile.as_view(),name="profile-detail") , 
    path("posteradd/",views.PostView.as_view(),name='post'),
    path("postview/",views.PostList.as_view(),name="index1"),
    path("postdelete/<int:pk>",views.PostdeleteView.as_view(),name="delete"),
    path("comment/<int:pk>/add/",views.CommentCreateView.as_view(),name="cmt-add"),
    path("api/", include("api.urls"))
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
