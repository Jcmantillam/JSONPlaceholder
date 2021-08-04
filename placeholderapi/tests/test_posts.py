from django.test import TestCase

import json

from rest_framework.test import APIClient
from rest_framework import status

from placeholderapi.models import BlogUser, Post
from placeholderapi.constants import API_POST

from decouple import config

class PostTestCase(TestCase):

    def setUp(self):

        BlogUser.objects.create(
            name="name",
            username="cmantillam",
            email="email@email.com",
            address={},
            phone="11111111",
            website="www.web.com",
            company={}
        )


    def test_create_post(self):
        client = APIClient()

        user = BlogUser.objects.all()
        test_post_data = {
            "title": "This is a Post",
            "body": "Hello this is another post",
            "blog_user": user.first().id
        }

        service = config('HOSTING') + API_POST
        response = client.post(
            service, 
            test_post_data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('title', result)
        self.assertIn('body', result)

        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_post_data)

    def test_get_user(self):

        client = APIClient()

        user = BlogUser.objects.all()
        Post.objects.create(
            title="This is a Post",
            body="Hello this is another post",
            blog_user=user.first()
        )

        service = config('HOSTING') + API_POST
        response = client.get(service)
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)


    def test_delete_user(self):

        client = APIClient()

        user = BlogUser.objects.all()
        post = Post.objects.create(
            title="This is a Post",
            body="Hello this is another post",
            blog_user=user.first()
        )


        service = config('HOSTING') + API_POST + f'{post.id}/'
        response = client.delete(
            service, 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        post_exists = Post.objects.filter(pk=post.id)
        self.assertFalse(post_exists)