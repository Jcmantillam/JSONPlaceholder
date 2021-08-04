from django.test import TestCase

import json

from rest_framework.test import APIClient
from rest_framework import status

from placeholderapi.models import BlogUser, Post, Comment, Album, Photo, Todo
from placeholderapi.constants import API_CONSULT

from decouple import config

class AlbumTestCase(TestCase):

    #Consult and save users tests
    def test_user_1(self):
        client = APIClient()

        test_consult_data = {
            "service" : "/users/1/",
            "save_result" : True
        }

        service = config('HOSTING') + API_CONSULT
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )
        users = list(BlogUser.objects.all())
        self.assertEqual(len(users), 1)


    def test_users(self):
        client = APIClient()

        test_consult_data = {
            "service" : "/users/",
            "save_result" : True
        }

        service = config('HOSTING') + API_CONSULT
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )
        users = list(BlogUser.objects.all())
        self.assertEqual(len(users), 10)
        

    #Consult and save posts tests
    def test_post_1(self):
        client = APIClient()

        test_consult_data = {
            "service" : "/posts/1/",
            "save_result" : True
        }

        service = config('HOSTING') + API_CONSULT
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )

        posts = list(Post.objects.all())
        users = list(BlogUser.objects.all())

        self.assertEqual(len(users), 1)
        self.assertEqual(len(posts), 1)


    def test_posts(self):
        client = APIClient()

        #saving the 100 posts
        test_consult_data = {
            "service" : "/posts/",
            "save_result" : True
        }

        service = config('HOSTING') + API_CONSULT
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )
        posts = list(Post.objects.all())
        self.assertEqual(len(posts), 100)


    def test_album(self):
        client = APIClient()

        #saving album and user
        test_consult_data = {
            "service" : "/albums/1",
            "save_result" : True
        }

        service = config('HOSTING') + API_CONSULT
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )
        album = list(Album.objects.all())
        users = list(BlogUser.objects.all())

        self.assertEqual(len(album), 1)
        self.assertEqual(len(users), 1)


    def test_comment(self):
        client = APIClient()

        #saving album and user
        test_consult_data = {
            "service" : "/comments/1",
            "save_result" : True
        }

        service = config('HOSTING') + API_CONSULT
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )
        comments = list(Comment.objects.all())
        post = list(Post.objects.all())

        self.assertEqual(len(comments), 1)
        self.assertEqual(len(post), 1)


    def test_photo(self):
        client = APIClient()

        #saving album and user
        test_consult_data = {
            "service" : "/photos/1",
            "save_result" : True
        }

        service = config('HOSTING') + API_CONSULT
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )
        album = list(Album.objects.all())
        photo = list(Photo.objects.all())

        self.assertEqual(len(photo), 1)
        self.assertEqual(len(album), 1)


    def test_todo(self):
        client = APIClient()

        #saving album and user
        test_consult_data = {
            "service" : "/todos/1",
            "save_result" : True
        }

        service = config('HOSTING') + API_CONSULT
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )
        users = list(BlogUser.objects.all())
        todo = list(Todo.objects.all())

        self.assertEqual(len(todo), 1)
        self.assertEqual(len(users), 1)
