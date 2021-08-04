from django.shortcuts import render
from .models import BlogUser, Post, Comment, Album, Photo, Todo
from .serializers import (
    BlogUserSerializer,
    PostSerializer,
    CommentSerializer,
    AlbumSerializer,
    PhotoSerializer,
    TodoSerializer,
    ConsumeServiceSerializer,
)
from .services import consult_process
from rest_framework import viewsets, generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class BlogUserViewset(viewsets.ModelViewSet):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer

    def get_queryset(self):
        users = BlogUser.objects.all()

        username = self.request.GET.get('username')

        if username:
            users = BlogUser.filter(nombre__contains=username)

        return users


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Post.objects.all()

        title = self.request.GET.get('title')

        if title:
            users = BlogUser.filter(nombre__contains=title)

        return posts


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewset(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(["POST"])
def ConsultPlaceholderServices(request):
    serializer = ConsumeServiceSerializer(data=request.data)
    if serializer.is_valid():
        data = consult_process(data=request.data)
        return Response(data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
