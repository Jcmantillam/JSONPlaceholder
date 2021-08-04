from .models import BlogUser, Post, Comment, Album, Photo, Todo
from rest_framework import serializers


class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
         model = BlogUser
         fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
         model = Post
         fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
         model = Comment
         fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
         model = Album
         fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
         model = Photo
         fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
         model = Todo
         fields = '__all__'


'''
It is is used on the endpoint to consume JSONPlaceholder
you can clarify if you want to save the result in the local BD
'''
class ConsumeServiceSerializer(serializers.Serializer):
    service = serializers.CharField(max_length=200)
    save_result = serializers.BooleanField()
