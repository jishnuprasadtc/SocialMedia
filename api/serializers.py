from rest_framework import serializers


from socialmedia import models
from socialmedia.models import Post



from django.contrib.auth.models import User


class userSerialiser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"
        read_only_fields=["id","user","created_at","updated_at","like"]