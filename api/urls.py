from django.urls import path
from api import views

from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router=router.register("post",views.PostView,basename="post-view")


urlpatterns=[
    path("register/",views.SignUpViews.as_view()),
    path("token/",ObtainAuthToken.as_view()),


]