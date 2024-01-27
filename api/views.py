from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication 
from rest_framework import permissions 


from api.serializers import userSerialiser,PostSerializer

from socialmedia.models import Post

# Create your views here.


class SignUpViews(APIView):
    def post(self,request,*args,**kwargs):
        serialiser=userSerialiser(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(data=serialiser.data)
        else:
            return Response(data=serialiser.errors)


class PostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
      return Post.objects.filter(user=self.request.user)


    



